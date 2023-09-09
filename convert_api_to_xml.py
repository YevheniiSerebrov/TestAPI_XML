import requests
import xml.etree.ElementTree as ET
# запускаєш цей файл, оновлюється файл OL_xml_my, потім записується з нормальними id, newXml.xml - кінцевий файл, який треба оновити на епіцентр
# URL API, откуда вы хотите получить XML
api_url = "http://ol.partners/api/ApiXml_v2/474e3fd5-d566-440e-9d34-30229dd6dd84"

try:
    # Отправляем GET-запрос
    response = requests.get(api_url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Получаем содержимое XML
        xml_data = response.text

        # Сохраняем данные в файл
        with open("OL_xml_my.xml", "w", encoding="utf-8") as xml_file:
            xml_file.write(xml_data)

        print("XML-данные успешно сохранены в файл OL_xml_final.xml")
    else:
        print("Ошибка при получении данных. Код состояния:", response.status_code)

except Exception as e:
    print("Произошла ошибка:", str(e))

tree = ET.parse('OL_xml_my.xml')
root = tree.getroot()

# Iterate through all offer elements
for offer in root.findall(".//offer"):
    vendor_code = offer.find("vendorCode").text
    offer.set("id", vendor_code)

# Save the modified XML to a new file
tree.write('newXml.xml', encoding='utf-8', xml_declaration=True)
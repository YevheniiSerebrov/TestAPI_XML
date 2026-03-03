import requests
import xml.etree.ElementTree as ET
import os
# Get the directory where the script is located
base_path = os.path.dirname(os.path.abspath(__file__))

# Use this path for all files
input_file = os.path.join(base_path, "OL_xml_my.xml")
output_file = os.path.join(base_path, "newXml.xml")
# запускаєш цей файл, оновлюється файл OL_xml_my, потім записується з нормальними id, newXml.xml - кінцевий файл, який треба оновити на епіцентр
# URL API, откуда вы хотите получить XML
api_url = "https://back-prod.olinfrastructure.com/b2b/product-export/file/71541BF1-E7C1-4335-B6DD-A31E05F89989/xml"


try:
    # Отправляем GET-запрос
    response = requests.get(api_url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Получаем содержимое XML
        xml_data = response.text

        # Сохраняем данные в файл
        #with open("OL_xml_my.xml", "w", encoding="utf-8") as xml_file:
            #xml_file.write(xml_data)
        with open(input_file, "w", encoding="utf-8") as xml_file:
            xml_file.write(xml_data)
        print("XML-данные успешно сохранены в файл OL_xml_final.xml")
    else:
        print("Ошибка при получении данных. Код состояния:", response.status_code)

except Exception as e:
    print("Произошла ошибка:", str(e))

#tree = ET.parse('OL_xml_my.xml')
#root = tree.getroot()

# ... (your parsing code) ...
tree = ET.parse(input_file)
# ...
tree.write(output_file, encoding='utf-8', xml_declaration=True)
# Iterate through all offer elements
for offer in root.findall(".//offer"):
    vendor_code = offer.find("vendorCode").text
    offer.set("id", vendor_code)

# Save the modified XML to a new file

tree.write('newXml.xml', encoding='utf-8', xml_declaration=True)

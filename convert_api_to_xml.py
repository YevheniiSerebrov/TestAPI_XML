import requests
import xml.etree.ElementTree as ET
import os

# 1. Setup paths correctly for GitHub environment
base_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(base_path, "OL_xml_my.xml")
output_file = os.path.join(base_path, "newXml.xml")

api_url = "https://back-prod.olinfrastructure.com/b2b/product-export/file/71541BF1-E7C1-4335-B6DD-A31E05F89989/xml"

try:
    # 2. Fetch the data
    response = requests.get(api_url)

    if response.status_code == 200:
        xml_data = response.text
        with open(input_file, "w", encoding="utf-8") as xml_file:
            xml_file.write(xml_data)
        print(f"XML data saved to {input_file}")
    else:
        print("Error fetching data. Status code:", response.status_code)
        exit(1) # Stop the script if the API is down

    # 3. Process the XML
    tree = ET.parse(input_file)
    root = tree.getroot()

    # 4. Iterate and update VendorCodes
    for offer in root.findall(".//offer"):
        vendor_code_elem = offer.find("vendorCode")
        if vendor_code_elem is not None:
            vendor_code = vendor_code_elem.text
            offer.set("id", vendor_code)

    # 5. Save the final file using the path we defined at the top
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"Final XML saved to {output_file}")

except Exception as e:
    print("An error occurred:", str(e))
    exit(1)

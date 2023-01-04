import json
import xmltodict

with open("01_input.xml", 'r') as xml_file:
    data_dict = xmltodict.parse(xml_file.read())

print(data_dict['response']['attribute']['mapOfMaps']['entryMap'])


json_data = json.dumps(data_dict)

# with open("data.json", "w") as json_file:
#         json_file.write(json_data)
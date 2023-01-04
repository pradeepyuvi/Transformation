import xml.etree.ElementTree as ET
tree = ET.parse('01_input.xml')
root = tree.getroot()
# print(root.attrib)
# print(root.iter('type'))
# with open('01_input.xml', 'r') as f:
#     data = f.read()
# startingData=data.replace('''<attribute name="status_code" value="1001" />
#           <attribute name="status_detail" value="OK" />''',"")
# startingData1=startingData.replace('''<attribute name="status_code" value="1001" />
#   <attribute name="status_detail" value="OK" />''',"")
# mapOfActionResponses_remove=startingData1.replace("mapOfActionResponses","mapOfActions")
# chnge_strtime=mapOfActionResponses_remove.replace('''<attribute name="starttime">''','''<attribute name="phase_action">''')
# strPhase=chnge_strtime.replace("STATUS_RESPONSE","CREATE_JOB_DEF",1)
# print(strPhase)

def createFile(inputData):
    with open("01_input.xml", "w") as xml_file:
        xml_file.write(inputData)

def readFile():
    with open('01_input.xml', 'r') as f:
        xmlData = f.read()
    startingData=xmlData.replace('''<attribute name="status_code" value="1001" />
          <attribute name="status_detail" value="OK" />''',"")
    startingData1=startingData.replace('''<attribute name="status_code" value="1001" />
    <attribute name="status_detail" value="OK" />''',"")
    mapOfActionResponses_remove=startingData1.replace("mapOfActionResponses","mapOfActions")
    chnge_strtime=mapOfActionResponses_remove.replace('''<attribute name="starttime">''','''<attribute name="phase_action">''')
    strPhase=chnge_strtime.replace("STATUS_RESPONSE","CREATE_JOB_DEF",1)
    return strPhase



def write_to_xml_file(name):
    file_data = readFile()
    result = file_data.replace(f'''</mapOfActions>
  </attribute>
  <attribute name="{name}">
    <mapOfActions>''', '')
    createFile(result)
    
for child in root.iter():
    childs = child.tag
    if childs[-8:] == 'entryMap':
        name = child.attrib.get('name')
        attrib_name = 'condition_name' if name.startswith('conditional') else 'PHASE'
        form_attrib_tag = f'''<attribute name="{attrib_name}" value="{name}"/>'''
        child.insert(3, form_attrib_tag)
        write_to_xml_file(name)       
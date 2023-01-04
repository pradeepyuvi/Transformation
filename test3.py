with open('01_input.xml', 'r') as f:
    data = f.read()
startingData=data.replace('''<attribute name="status_code" value="1001" />
          <attribute name="status_detail" value="OK" />''',"")
startingData1=startingData.replace('''<attribute name="status_code" value="1001" />
  <attribute name="status_detail" value="OK" />''',"")
mapOfActionResponses_remove=startingData1.replace("mapOfActionResponses","mapOfActions")
chnge_strtime=mapOfActionResponses_remove.replace('''<attribute name="starttime">''','''<attribute name="phase_action">''')
print(chnge_strtime)
import xml.etree.ElementTree as ET

try:
    # Try to parse the XML file
    tree = ET.parse('01_input.xml')
except ET.ParseError:
    # If the parse fails, the XML file is not well-formed
    print('XML file is not valid')
else:
    # If the parse succeeds, the XML file is well-formed
    print('XML file is valid')

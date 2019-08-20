def read_xml_file(files):
  import xml.etree.ElementTree as ET
  import os 
  
  tree = ET.parse(files[0])
  root = tree.getroot()
  
  for file in files:
    os.remove(file)
  
  return root
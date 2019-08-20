def read_xml_file(file_path):
  import xml.etree.ElementTree as ET
  import os 
  
  tree = ET.parse(file_path)
  root = tree.getroot()
  
  os.remove(file_path)
  
  return root
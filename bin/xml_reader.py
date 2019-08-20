def read_xml_file(file_path):
  import xml.etree.ElementTree as ET
  import os 
  
  tree = ET.parse(file_path)
  root = tree.getroot()
  
  # for file in files:
  #   os.remove(file)
  
  return root
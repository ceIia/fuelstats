import xml.etree.ElementTree as ET

def read_xml_file(file_path):
  tree = ET.parse(file_path)
  root = tree.getroot()
  
  return root

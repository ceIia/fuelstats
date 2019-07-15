import xml.etree.ElementTree as ET

tree = ET.parse('public/data.xml')
root = tree.getroot()
p = []
pc = []

for pdv in root:
  for pr in pdv.iter('prix'):
    pc.append((pr.attrib['nom'], pr.attrib['valeur']))
  p.append((pdv.attrib['cp'], pdv.findall('ville')[0].text, ('prices', pc)))
  pc = []

def search(psc):
  for i in p:
    if i[0] == psc:
      print i
      return i
      break
    else :
      print('not found')

# search('06500')
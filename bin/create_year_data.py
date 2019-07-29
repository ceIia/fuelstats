from datetime import datetime
from bin.geosearch import geosearch

def create_raw_array(xml_data, postcode, address, key):
  pump_list = []
  raw_array = []
  for raw_entry in xml_data:
    pump_list.append(raw_entry)
  
  for pump_element in pump_list:
    pump_element_price_list = []
    pump_state = True
    
    if pump_element.iter('prix') and int(pump_element.attrib['cp']) == postcode:
      legacy_address = pump_element.find('adresse').text
      for pump_element_price_data in pump_element.iter('prix'):
        try:
          # handle times when the date is weirdly formated
          try:
            fuel_lastprice = datetime.strptime(pump_element_price_data.attrib['maj'], '%Y-%m-%dT%H:%M:%S')
          except ValueError:
            fuel_lastprice = datetime.strptime(pump_element_price_data.attrib['maj'], '%Y-%m-%d %H:%M:%S')
          pump_element_price_list.append((pump_element_price_data.attrib['nom'], fuel_lastprice, pump_element_price_data.attrib['valeur']))
        except KeyError:
          pump_state = False
      if int(pump_element.attrib['cp']) == postcode:
        geographical_information = geosearch(pump_element.attrib['latitude'], pump_element.attrib['longitude'], address, legacy_address, pump_element.attrib['id'], key)
      else:
        geographical_information = None
      
      print(geographical_information)
      if geographical_information != None and int(pump_element.attrib['cp']) == postcode and pump_state:
        raw_array.append((geographical_information, pump_element_price_list))
      else:
        pass
  return raw_array

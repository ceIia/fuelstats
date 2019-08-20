import requests as requests

def geosearch(latitude, longitude, address, legacy_address, id, key):
  
  url_lat = float(latitude)/100000
  url_lon = float(longitude)/100000
  max_radius = "200"

  url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(url_lat) + "," + str(url_lon) + "&key=" + key + "&type=gas_station&radius=" + max_radius
  
  distance_request_url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=" + address + "&destinations=" + str(url_lat) + "," + str(url_lon) + "&key=" + key

  calculated_distance = geosearch = requests.get(distance_request_url)
  distance_json = calculated_distance.json()
  distance = distance_json['rows'][0]['elements'][0]['distance']['text']
  
  print("\n Starting geosearch for pump " + str(id) + ".")
  geosearch = requests.get(url)
  data = geosearch.json()

 
  if data['status'] == "ZERO_RESULTS":
    n = 8
    print('pump ID: ' + str(id) + " / legacy address: " + legacy_address)
    print("no results were found within the standard range of " + str(max_radius) + " meters.")
    failover_radius = int(max_radius)
    while n > 0:
      print("expanding by 50 meters")
      n -= 1
      failover_radius += 50
      further_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(url_lat) + "," + str(url_lon) + "&key=" + key + "&type=gas_station&radius=" + str(failover_radius)
      print("current range: " + str(failover_radius) + " url: " + further_url)
      
      geosearch = requests.get(further_url)
      data = geosearch.json()
      
      print("google data status: " + data['status'])
      if data['status'] == "OK":
        print("gas station type result found.")
        break
      
    if data['status'] == "ZERO_RESULTS":
      print("no results were found within the extended range of: " + str(failover_radius) + " meters.")
      misc_radius = "350"
      print("trying supermarket type with a range of " + str(misc_radius) + " meters.")
      failover_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(url_lat) + "," + str(url_lon) + "&key=" + key + "&type=supermarket&radius=" + misc_radius
      
      geosearch = requests.get(failover_url)
      data = geosearch.json()
      if data['status'] == "OK":
        print("supermarket type result found.")
      

    if data['status'] == "ZERO_RESULTS":
      print("no results were found within the gas station nor supermarket type. skipping gas station ID " + str(id) + ".")
      geosearch_result = None
      return geosearch_result
  
  print("Geosearch for pump " + str(id) + " is done.")
  name = data['results'][0]['name']
  address = data['results'][0]['vicinity']
  place_lat = data['results'][0]['geometry']['location']['lat']
  place_lng = data['results'][0]['geometry']['location']['lng']
  pump_id = data['results'][0]['id']
  place_type = data['results'][0]['types'][0]
  image_url = "https://maps.googleapis.com/maps/api/staticmap?size=400x200&zoom=12&maptype=roadmap\&markers=size:mid%7Ccolor:red%7C" + str(place_lat) + "," + str(place_lng) + "&key=" + key
  
  geosearch_result = (name, address, image_url, distance, pump_id, legacy_address, id, place_type)

  return geosearch_result
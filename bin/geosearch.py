import requests as requests

def geosearch(latitude, longitude, address, legacy_address, id, key):
  
  url_lat = float(latitude)/100000
  url_lon = float(longitude)/100000
  max_radius = "200"

  url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(url_lat) + "," + str(url_lon) + "&key=" + key + "&type=gas_station&radius=" + max_radius
  failover_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(url_lat) + "," + str(url_lon) + "&key=" + key + "&type=supermarket&radius=" + max_radius
  
  distance_request_url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=" + address + "&destinations=" + str(url_lat) + "," + str(url_lon) + "&key=" + key

  calculated_distance = geosearch = requests.get(distance_request_url)
  distance_json = calculated_distance.json()
  distance = distance_json['rows'][0]['elements'][0]['distance']['text']

  geosearch = requests.get(url)
  data = geosearch.json()
  
  if data['status'] == "ZERO_RESULTS":
    geosearch = requests.get(failover_url)
    data = geosearch.json()

    if data['status'] == "ZERO_RESULTS":
      geosearch_result = None
      return geosearch_result
  
  name = data['results'][0]['name']
  address = data['results'][0]['vicinity']
  place_lat = data['results'][0]['geometry']['location']['lat']
  place_lng = data['results'][0]['geometry']['location']['lng']
  pump_id = data['results'][0]['id']
  image_url = "https://maps.googleapis.com/maps/api/staticmap?size=400x200&zoom=12&maptype=roadmap\&markers=size:mid%7Ccolor:red%7C" + str(place_lat) + "," + str(place_lng) + "&key=" + key
  
  geosearch_result = (name, address, image_url, distance, pump_id, legacy_address, id)

  return geosearch_result
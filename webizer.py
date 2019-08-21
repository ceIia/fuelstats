from flask import Flask, render_template, request
from bin.archive_downloader import download_archive
from bin.xml_reader import read_xml_file
from bin.create_year_data import create_raw_array
from bin.create_year_averages import yearly_average_constructor
from bin.sorting import *
from bin.generate_statistics import *  
from dotenv import load_dotenv
import calendar, json, time, os, requests 
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

load_dotenv()

sentry_sdk.init(
    dsn="https://" + os.getenv("SENTRY_DSN_URL"),
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('input.html', key = os.getenv("GOOGLE_MAPS_API_KEY"))

@app.route('/results',methods = ['POST', 'GET'])
def result():
   start = time.time()
   months_abbr = []
   months_full = []
   essence_types = ['gazole', 'sp98', 'e10', 'e85', 'gplc']

   for i in range(1, 13):
      months_abbr.append(calendar.month_abbr[i])
      months_full.append(calendar.month_name[i])
   
   if request.method == 'POST':
      location = request.form['location']
          
      key = os.getenv("GOOGLE_MAPS_API_KEY")
      
      postcode_request_url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + str(location) + "&key=" + key

      postcode_geosearch = requests.get(postcode_request_url)
      data = postcode_geosearch.json()
      
      postcode = [int(address["long_name"]) for address in data['results'][0]["address_components"] if "postal_code" in address["types"]][0]
      
      # files = download_archive(os.getenv("DATA_ARCHIVE_NAME"), os.getenv("S3_BUCKET_NAME"))
      
      xml_data = read_xml_file(os.getenv("PATH_TO_DATA") + os.getenv("DATA_ARCHIVE_NAME") + '.xml')
       
      raw_array = create_raw_array(xml_data, postcode, location, key)
      
      pumps_infos = build_pump_list_infos(raw_array)
      
      now_time = time.strftime('%d/%m/%Y @ %T')
      
      results_length = len(raw_array)
      essence_types_length = len(essence_types)
      
      avg_minimums_by_essence_type = avg_minimums(raw_array)
      average_by_essence_type = avg_by_essence_type(raw_array)
      average_by_essence_type_totalb = avg_by_essence_type_totalb(raw_array)
      sorted_by_essence_type = sort_by_essence_type(raw_array)
      sorted_by_essence_type_totalb = sort_by_essence_type_totalb(raw_array)
      totalb_average = get_total_monthly_average(raw_array)
      non_totalb_average = get_non_total_monthly_average(raw_array)
      getback = yearly_average_constructor(raw_array)

      del raw_array
      # getback_json = json.dumps(getback)
     
      end = time.time()
      process_time = end - start
      return render_template("results.html", 
                             getback = getback, 
                             months_abbr = months_abbr, 
                             months_full = months_full, 
                             pumps_infos = pumps_infos, 
                             totalb_average = totalb_average, 
                             non_totalb_average = non_totalb_average, 
                             sorted_by_essence_type = sorted_by_essence_type, 
                             sorted_by_essence_type_totalb = sorted_by_essence_type_totalb,
                             postcode = postcode,
                             time = now_time, 
                             address = location,
                             results_length = results_length,
                             essence_types_length = essence_types_length,
                             essence_types = essence_types,
                             average_by_essence_type = average_by_essence_type,
                             average_by_essence_type_totalb = average_by_essence_type_totalb,
                             avg_minimums_by_essence_type = avg_minimums_by_essence_type,
                             process_time = process_time
                             )

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True)
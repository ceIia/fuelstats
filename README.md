# fuelstats [![Build Status](https://travis-ci.com/ceIia/fuelstats.svg?token=w3quvxVc78RmD2Dzryak&branch=master)](https://travis-ci.com/ceIia/fuelstats)
fuelstats is an app that allows you to get differents dynamic stats around fuel prices in France. 🥖


## Project setup
1. install python>3.7
2. download your yearly archive from [here](https://www.prix-carburants.gouv.fr/rubrique/opendata/) and add it to the root of the fuelstats folder
3. edit `webizer.py` to use your archive file (*refer to the how-to section for this*)

> note : you will need an internet connection and a Google Maps API access (*paid*) for **fuelstats** to work correctly

## How-to

**Clone this project**
```
git clone https://github.com/ceIia/fuelstats
```

**Get a Google Maps API key**
1. Log in to the [Google Cloud Platform Console](https://console.cloud.google.com/home)
2. Setup a project with the following accesses : `Places API`, `Distance Matrix API`, `Maps Static API` and `Geocoding API`.
3. Make sure to secure the usage of your API key as it will be publicly available (*limit the access to your domain-s*).
4. Copy your API key and go on to the next step.

**Setup API keys**
1. Rename `.env.simple` to `.env`
2. Edit the file and add your API key

```
GOOGLE_MAPS_API_KEY=your_key_here
```

**Edit `webizer.py`**
```py
xml_data = read_xml_file('YOUR_FILE_NAME.xml')
```

**Start the flask webserver**
```
FLASK_APP=webizer.py python3 -m flask run --host=0.0.0.0
```

Add `FLASK_DEBUG=1` to the server start's command to run in debug mode.

---

*this project is made possible thanks to the french government. #bigdata*

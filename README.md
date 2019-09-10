# fuelstats [![Build Status](https://travis-ci.com/ceIia/fuelstats.svg?token=w3quvxVc78RmD2Dzryak&branch=master)](https://travis-ci.com/ceIia/fuelstats)
fuelstats is an app that allows you to get differents dynamic stats around fuel prices in France. 🥖
feel free to open issues or pull requests if you want/need to.


## Project pre-setup
1. install python>3.7
2. download your yearly archive from [here](https://www.prix-carburants.gouv.fr/rubrique/opendata/)
3. unzip your archive and add it to your folder of choice, and specify the path (`PATH_TO_DATA`) and the file name without the extension (`DATA_ARCHIVE_NAME`) separately in your .env file. (_xml files only_)

> note : you will need an internet connection, a Sentry account (for bug tracking in production environments - optional, but you'll have to do some code adjusting if you decide not to use it) and a Google Maps API access (*paid*) for **fuelstats** to work correctly.

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
1. Rename `.env.sample` to `.env`
2. Edit the file and configure the values

_Example :_
```
GOOGLE_MAPS_API_KEY=your_key_here <== replace the value after the equal sign
```

**Install fuelstats dependencies**
(_cd into root clone folder before_)
```
pip3 install -r requirements.txt
(if it fails) python3 -m pip install -r requirements.txt
```

**Start the production server**
```
gunicorn3 --bind unix:fuelstats.sock -m 007 webizer:app -b 0.0.0.0:80 --timeout 300
```
I recommend you create a unix service to run the gunicorn instance for fuelstats so you can get better CI integration, error handling, clean logging and seamless runtimes.

**Start the flask webserver (DEVELOPMENT ONLY)**
```
FLASK_DEBUG=1 FLASK_APP=webizer.py python3 -m flask run --host=0.0.0.0
```
**Only use the built-in Flask server for development purposes, use gunicorn for productionn purposes. If a critical error occurs, the whole flask server will crash, requiring manual restart. Using an actual WSGI server will provide stability and better logging.** 

---

*this project was made possible thanks to the french government. #bigdata*

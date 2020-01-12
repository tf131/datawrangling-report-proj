# Duplicate detection on a generic restaurant databaseusing different geocoding providers
## Getting Started
Clone the repository to your local machine and change to that directory.

```
git clone https://github.com/tf131/datawrangling-report-proj.git
cd .\datawrangling-report-proj\

```

### Prerequisites
The runtime environment for this project were:
* Windows 10 Pro Version 10.0.19536 Build 19536
* Python 3.8.1

**Code should also work on any Linux distribution and MacOS with installed > Python 3.7**

### Installing on Windows
Check if python is working and you run version 3.7 or higher.
```
python -V
>> Python 3.8.1
```
If getting issues, check: https://geek-university.com/python/add-python-to-the-windows-path/


create a new Python virtualenv and activate it
```
python -m venv ./venv
venv\Scripts\activate
```

install python requirements
`pip install -r requirements.txt`

open *conf.ini* in a text editor of your choice and replace the dummy API keys. They can be created for free at their websites below.
1. here geocoder: https://developer.here.com/
1. google place search: https://developers.google.com/places/web-service/search 
1. geocodio: https://www.geocod.io/docs/
1. mapbox: https://docs.mapbox.com/api/





1. on debian based os, install virtualenv driver
`sudo apt-get install python38-venv`
1. create a new PHYTHON3.8 environment, activate it and install all requirements
`python -m venv ./venv`
1. activate your virtualenv
1.1. debian based: `source venv/bin/activate`
1.1. windows: `venv\Scripts\activate`
1. upgrade pip (optional)
`python -m pip install --upgrade pip`
1. install requirements
`pip install -r requirements.txt`
3. The config file conf.ini has to be adapted - create your own API Keys for: 
1.1. here geocoder: https://developer.here.com/
1.1. google place search: https://developers.google.com/places/web-service/search 
1.1. geocodio: https://www.geocod.io/docs/
1.1. Fill in your mongoDB connection string
1. run the main function

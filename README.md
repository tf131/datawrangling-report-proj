# Duplicate detection on a generic restaurant database using different geocoding providers
*Dataset: https://hpi.de/naumann/projects/repeatability/datasets/restaurants-dataset.html*
## Getting Started
Clone the repository to your local machine and navigate to that directory.

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



### Installing on Debian based Linux
Check if python is working and you run version 3.7 or higher.
```
python -V
>> Python 3.8.1
```

install virtualenv driver for your python version. (here: python38-venv)
`sudo apt-get install python38-venv`
create a new Python virtualenv and activate it
```
python -m venv venv
source venv/bin/activate
```
install python requirements
`pip install -r requirements.txt`

open *conf.ini* in a text editor of your choice and replace the dummy API keys. They can be created for free at their websites below.
1. here geocoder: https://developer.here.com/
1. google place search: https://developers.google.com/places/web-service/search 
1. geocodio: https://www.geocod.io/docs/
1. mapbox: https://docs.mapbox.com/api/
1. connection string to your mongoDB instance (either local or on https://www.mongodb.com/cloud/atlas)
1. define a database name for mongoDB, which is used

### Run code
call the main function
`python main.py`

```python
def main():
    # get mongoDB collection object. Used for any further mongodb querys.
    mongodb_collection = get_mongodb_db_collection()
    # fill the mongodb collection with initial data from
    # https://hpi.de/naumann/projects/repeatability/datasets/restaurants-dataset.html
    initial_fill_database(mongodb_collection)
    # link database to api providers
    link_to_hereapi(mongodb_collection, api_key=config['api_keys']['here'])
    link_to_googleplaceapi(mongodb_collection, api_key=config['api_keys']['googleplaces'])
    link_to_geocodio(mongodb_collection, config['api_keys']['geocodio'])
    #calculate precision, recall and f1score
    calcer(mongodb_collection, unique_identifiers)

    # optional: plot location information to map (based on Google place search)
    mapplot(mongodb_collection, api_key=config['api_keys']['mapbox'])
```
## Authors

* **Tim Fischer** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md)

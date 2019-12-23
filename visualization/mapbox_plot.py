from pymongo import MongoClient
import numpy as np
import pandas as pd
import plotly.express as px


def get_mongodb_db(db_name):
    client = MongoClient(
        "mongodb+srv://tim:fxPgQrWtKb8MY2x5FtkY@cluster4report-dmdb-4pvyi.mongodb.net/test?retryWrites=true&w=majority")
    return client[db_name]


db = get_mongodb_db("restaurants")
collection = db["restaurants_basic"]

query = {
    'google_place_search_api_result.geometry.location': {
        '$exists': 1
    }
}

projection = {'id': 1, 'name': 1, '_id': 0, 'google_place_search_api_result.geometry.location.lat': 1,
              'google_place_search_api_result.geometry.location.lng': 1}
results_raw = collection.find(query, projection)
df = pd.DataFrame(columns=['id', 'name', 'lat', 'lng'])
list_of_dicts = list()
for elem in results_raw:
    id = elem['id']
    name = elem['name']
    lat = elem['google_place_search_api_result']['geometry']['location']['lat']
    lng = elem['google_place_search_api_result']['geometry']['location']['lng']
    dict_ = {"id": id, "name": name, "latitude": lat, "longitude": lng}
    list_of_dicts.append(dict_)
df = pd.DataFrame.from_dict(list_of_dicts, orient='columns')
print(df.head(5))
BBox = ((df.longitude.min(), df.longitude.max(),
         df.latitude.min(), df.latitude.max()))

px.set_mapbox_access_token("pk.eyJ1IjoibWl0NjU3MTgiLCJhIjoiY2s0YjdwZDNnMGI1dzNtbml2Y3RiMXB4NCJ9.cVDohXL8S_jFoRm1I-x_TQ")
fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", text="id")
fig.show()
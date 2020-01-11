from pymongo import MongoClient
import numpy as np
import pandas as pd
import plotly.express as px
import logging
import configparser


def mapplot(mongodb_collection, api_key):
    query = {
        'google_place_search_api_result.geometry.location': {
            '$exists': 1
        }
    }

    projection = {'id': 1, 'name': 1, '_id': 0, 'google_place_search_api_result.geometry.location.lat': 1,
                  'google_place_search_api_result.geometry.location.lng': 1, 'google_place_search_api_result.name': 1}
    results_raw = mongodb_collection.find(query, projection)
    df = pd.DataFrame(columns=['id', 'name', 'lat', 'lng', 'formatted_name', 'size'])
    list_of_dicts = list()
    for elem in results_raw:
        size = 7
        id = elem['id']
        formatted_name = elem['google_place_search_api_result']['name']
        name = elem['name']
        lat = elem['google_place_search_api_result']['geometry']['location']['lat']
        lng = elem['google_place_search_api_result']['geometry']['location']['lng']
        dict_ = {"id": id, "name": name, "latitude": lat, "longitude": lng, "formatted_name": formatted_name,
                 "size": size}
        list_of_dicts.append(dict_)
    df = pd.DataFrame.from_dict(list_of_dicts, orient='columns')

    BBox = ((df.longitude.min(), df.longitude.max(),
             df.latitude.min(), df.latitude.max()))

    px.set_mapbox_access_token(api_key)
    # fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", text="formatted_name", zoom=4)
    # fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", zoom=4, size="size")
    fig = px.density_mapbox(df, lat="latitude", lon="longitude", radius=25, zoom=2, mapbox_style="light")
    fig.show()

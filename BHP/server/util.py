import json
import pickle
import numpy as np

__locations=None
__data_columns=None
__model=None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1
    x_ = np.zeros(len(__data_columns))
    x_[0] = sqft
    x_[1] = bath
    x_[2] = bhk
    if loc_index >= 0:
        x_[loc_index] = 1
    return round(__model.predict([x_])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading sabed artifacts...start")
    global __data_columns
    global __locations
    with  open("./artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open("./artifacts/bangalore_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
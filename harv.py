from math import radians, cos, sin, asin, sqrt

def haversine(x,y):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [x[0], x[1], y[0], y[1]])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r



import pandas as pd
from ast import literal_eval
trainSet = pd.read_csv('./train_set.csv',converters={"Trajectory": literal_eval},index_col='tripId')
trainSet = trainSet[0:25]
print trainSet
print haversine(trainSet["Trajectory"][1][1][1:],trainSet["Trajectory"][6][1][1:])

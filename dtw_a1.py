import pandas as pd
import numpy as np
from ast import literal_eval
import csv
from dtw import dtw

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

# read test set and make lon-lat lists
trajectory_list = []
with open('./test_set_a1.csv','rb') as csvfile:
    for row in csvfile:
        trajectory_list.append(row)
trajectory_list.pop(0)
trajectory_list = [literal_eval(x) for x in trajectory_list]

lonlat1 = []
lonlat2 = []
lonlat3 = []
lonlat4 = []
lonlat5 = []
for x in trajectory_list[0]:
    lonlat1.append((x[1],x[2]))
for x in trajectory_list[1]:
    lonlat2.append((x[1],x[2]))
for x in trajectory_list[2]:
    lonlat3.append((x[1],x[2]))
for x in trajectory_list[3]:
    lonlat4.append((x[1],x[2]))
for x in trajectory_list[4]:
    lonlat5.append((x[1],x[2]))

# read train set and make lon-lat lists

trajectory_list = []
trainSet = pd.read_csv('./train_set.csv',converters={"Trajectory": literal_eval},index_col='tripId')
trainSet = trainSet[0:20]
for x in trainSet["Trajectory"]:
    #print line
    trajectory_list.append(x)

print trajectory_list[0][0]


# get for each pair the dtw distances and store them in closest
closest = []
index = 0
for trip in trajectory_list:
    lonlattest = []
    for x in trip:
        lonlattest.append([x[1],x[2]])
    d = dtw(lonlat1,lonlattest,dist=haversine)
    closest.append(d)
    index+=1

print closest
#array = np.asarray(closest)
#minfive = arr.argsort()[:5]

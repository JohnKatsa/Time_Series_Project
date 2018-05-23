import pandas as pd
import numpy as np
from ast import literal_eval
import csv
from dtw import dtw

import time

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

# initialize time
start_time = time.time()

# read test set and make lon-lat lists
trajectory_list0 = []
with open('./test_set_a1.csv','rb') as csvfile:
    for row in csvfile:
        trajectory_list0.append(row)
trajectory_list0.pop(0)
trajectory_list0 = [literal_eval(x) for x in trajectory_list0]

lonlat1 = []
lonlat2 = []
lonlat3 = []
lonlat4 = []
lonlat5 = []
for x in trajectory_list0[0]:
    lonlat1.append((x[1],x[2]))
for x in trajectory_list0[1]:
    lonlat2.append((x[1],x[2]))
for x in trajectory_list0[2]:
    lonlat3.append((x[1],x[2]))
for x in trajectory_list0[3]:
    lonlat4.append((x[1],x[2]))
for x in trajectory_list0[4]:
    lonlat5.append((x[1],x[2]))

# read train set and make lon-lat lists

trajectory_list = []
journey_list = []
trainSet = pd.read_csv('./train_set.csv',converters={"Trajectory": literal_eval},index_col='tripId')
trainSet = trainSet[0:20]
for x, jpid in zip(trainSet["Trajectory"],trainSet["journeyPatternId"]):
    trajectory_list.append(x)
    journey_list.append(jpid)

print trajectory_list[0][0]


# get for pair 1 the dtw distances and store them in closest
closest1 = []
closest2 = []
closest3 = []
closest4 = []
closest5 = []
index = 0
for trip,journey in zip(trajectory_list,journey_list):
    lonlattest = []
    for x in trip:
        lonlattest.append([x[1],x[2]])
    dist1, cost1, acc1, path1 = dtw(lonlat1,lonlattest,dist=haversine)
    closest1.append(dist1)
    dist2, cost2, acc2, path2 = dtw(lonlat2,lonlattest,dist=haversine)
    closest2.append(dist2)
    dist3, cost3, acc3, path3 = dtw(lonlat3,lonlattest,dist=haversine)
    closest3.append(dist3)
    dist4, cost4, acc4, path4 = dtw(lonlat4,lonlattest,dist=haversine)
    closest4.append(dist4)
    dist5, cost5, acc5, path5 = dtw(lonlat5,lonlattest,dist=haversine)
    closest5.append(dist5)
    index+=1

#print closest
array1 = np.asarray(closest1)
minfive1 = array1.argsort(axis=0)[:5]
for i in minfive1:
    print "1", journey_list[i], closest1[i]

array2 = np.asarray(closest2)
minfive2 = array2.argsort(axis=0)[:5]
for i in minfive2:
    print "2", journey_list[i], closest2[i]

array3 = np.asarray(closest3)
minfive3 = array3.argsort(axis=0)[:5]
for i in minfive3:
    print "3", journey_list[i], closest3[i]

array4 = np.asarray(closest4)
minfive4 = array4.argsort(axis=0)[:5]
for i in minfive4:
    print "4", journey_list[i], closest4[i]

array5 = np.asarray(closest5)
minfive5 = array5.argsort(axis=0)[:5]
for i in minfive5:
    print "5", journey_list[i], closest5[i]

#calculate elapsed time
elapsed_time = time.time() - start_time
print "dt = ", elapsed_time, "sec" 

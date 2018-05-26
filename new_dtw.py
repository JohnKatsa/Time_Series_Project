import pandas as pd
import numpy as np
from ast import literal_eval
import csv
from dtw import dtw

import time
from operator import itemgetter

from math import radians, cos, sin, asin, sqrt

from gmplot import gmplot

def knn(closest):

    d = {}

    for x in closest:
        d[str(x[2])] = 0
        print x[2]

    for x in closest:
        d[str(x[2])] += 1

    max = d[str(closest[0][2])]
    maxjpid = closest[0][2]
    for key, value in d.iteritems():
        if value > max:
            max = value
            maxjpid = key

    print maxjpid
    return maxjpid

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
trainSet = pd.read_csv('./train_set.csv',converters={"Trajectory": literal_eval},index_col='tripId',nrows=200)


# read test set and make lon-lat lists
trajectory_list0 = []
with open('./test_set_a1.csv','rb') as csvfile:
    for row in csvfile:
        trajectory_list0.append(row)
trajectory_list0.pop(0)
trajectory_list0 = [literal_eval(x) for x in trajectory_list0]
index = 0

for route in trajectory_list0:
    lonlat=[]
    for x in route:
        lonlat.append((x[1],x[2]))

    trajectory_list = []
    journey_list = []
    for x, jpid in zip(trainSet["Trajectory"],trainSet["journeyPatternId"]):
        trajectory_list.append(x)
        journey_list.append(jpid)

    closest = []
    for trip,journey in zip(trajectory_list,journey_list):
        lonlattest = []
        for x in trip:
            lonlattest.append((x[1],x[2]))
        dist1, cost1, acc1, path1 = dtw(lonlat,lonlattest,dist=haversine)
        closest.append([dist1,lonlattest,journey])
    closest.sort(key=itemgetter(0))
    closest = closest[0:5]
    gmap = gmplot.GoogleMapPlotter(lonlat[0][1],lonlat[0][0], 13)
    lons, lats = zip(*lonlat)
    gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
# Draw
    file = "trip" + str(index) +".html"
    gmap.draw(file)
    for i in range(0,5):
        gmap = gmplot.GoogleMapPlotter(closest[i][1][0][1],closest[i][1][0][0], 13)
        temp = closest[i][1]
        lons, lats = zip(*temp)
        gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
    # Draw
        file = "trip" + str(index) +"_"+str(i)+".html"
        gmap.draw(file)
    index += 1
    total_time = time.time()-start_time#  time.time()
    start_time = time.time()
    print "total_time : %s\n====================\n\n" %(total_time)
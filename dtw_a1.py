import pandas as pd
import numpy as np
from ast import literal_eval
import csv
from dtw import dtw

import time
from operator import itemgetter

from math import radians, cos, sin, asin, sqrt

from gmplot import gmplot

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
trainSet = pd.read_csv('./train_set.csv',converters={"Trajectory": literal_eval},index_col='tripId',nrows=20)
#trainSet = trainSet[0:20]
for x, jpid in zip(trainSet["Trajectory"],trainSet["journeyPatternId"]):
    trajectory_list.append(x)
    journey_list.append(jpid)

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
        lonlattest.append((x[1],x[2]))
    dist1, cost1, acc1, path1 = dtw(lonlat1,lonlattest,dist=haversine)
    closest1.append([dist1,lonlattest,journey])
    dist2, cost2, acc2, path2 = dtw(lonlat2,lonlattest,dist=haversine)
    closest2.append([dist2,lonlattest,journey])
    dist3, cost3, acc3, path3 = dtw(lonlat3,lonlattest,dist=haversine)
    closest3.append([dist3,lonlattest,journey])
    dist4, cost4, acc4, path4 = dtw(lonlat4,lonlattest,dist=haversine)
    closest4.append([dist4,lonlattest,journey])
    dist5, cost5, acc5, path5 = dtw(lonlat5,lonlattest,dist=haversine)
    closest5.append([dist5,lonlattest,journey])
    index+=1

#print closest
closest1.sort(key=itemgetter(0))
closest1 = closest1[0:5]
gmap = gmplot.GoogleMapPlotter(lonlat1[0][1],lonlat1[0][0], 13)
lons, lats = zip(*lonlat1)
gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
# Draw
gmap.draw("trip1.html")
filenames = ["trip11.html","trip12.html","trip13.html","trip14.html","trip15.html"]
for i in range(0,5):
    gmap = gmplot.GoogleMapPlotter(closest1[i][1][0][1],closest1[i][1][0][0], 13)
    temp = closest1[i][1]
    lons, lats = zip(*temp)
    gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
    # Draw
    gmap.draw(filenames[i])

closest2.sort(key=itemgetter(0))
closest2 = closest2[0:5]
gmap = gmplot.GoogleMapPlotter(lonlat2[0][1],lonlat2[0][0], 13)
lons, lats = zip(*lonlat2)
gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
# Draw
gmap.draw("trip2.html")
filenames = ["trip21.html","trip22.html","trip23.html","trip24.html","trip25.html"]
for i in range(0,5):
    gmap = gmplot.GoogleMapPlotter(closest2[i][1][0][1],closest2[i][1][0][0], 13)
    temp = closest2[i][1]
    lons, lats = zip(*temp)
    gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
    # Draw
    gmap.draw(filenames[i])

closest3.sort(key=itemgetter(0))
closest3 = closest3[0:5]
gmap = gmplot.GoogleMapPlotter(lonlat3[0][1],lonlat3[0][0], 13)
lons, lats = zip(*lonlat3)
gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
# Draw
gmap.draw("trip3.html")
filenames = ["trip31.html","trip32.html","trip33.html","trip34.html","trip35.html"]
for i in range(0,5):
    gmap = gmplot.GoogleMapPlotter(closest3[i][1][0][1],closest3[i][1][0][0], 13)
    temp = closest3[i][1]
    lons, lats = zip(*temp)
    gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
    # Draw
    gmap.draw(filenames[i])

closest4.sort(key=itemgetter(0))
closest4 = closest4[0:5]
gmap = gmplot.GoogleMapPlotter(lonlat4[0][1],lonlat4[0][0], 13)
lons, lats = zip(*lonlat4)
gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
# Draw
gmap.draw("trip4.html")
filenames = ["trip41.html","trip42.html","trip43.html","trip44.html","trip45.html"]
for i in range(0,5):
    gmap = gmplot.GoogleMapPlotter(closest4[i][1][0][1],closest4[i][1][0][0], 13)
    temp = closest4[i][1]
    lons, lats = zip(*temp)
    gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
    # Draw
    gmap.draw(filenames[i])

closest5.sort(key=itemgetter(0))
closest5 = closest5[0:5]
gmap = gmplot.GoogleMapPlotter(lonlat5[0][1],lonlat5[0][0], 13)
lons, lats = zip(*lonlat5)
gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
# Draw
gmap.draw("trip5.html")
filenames = ["trip51.html","trip52.html","trip53.html","trip54.html","trip55.html"]
for i in range(0,5):
    gmap = gmplot.GoogleMapPlotter(closest5[i][1][0][1],closest5[i][1][0][0], 13)
    temp = closest5[i][1]
    lons, lats = zip(*temp)
    gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
    # Draw
    gmap.draw(filenames[i])

#calculate elapsed time
elapsed_time = time.time() - start_time
print "dt = ", elapsed_time, "sec"

import pandas as pd
import numpy as np
from ast import literal_eval
import csv
from dtw import dtw

import time
from operator import itemgetter

from math import radians, cos, sin, asin, sqrt

from gmplot import gmplot
from random import shuffle

def knn(closest):

    d = {}

    for x in closest:
        d[str(x[2])] = 0
       # print x[2]

    for x in closest:
        d[str(x[2])] += 1

    max = d[str(closest[0][2])]
    maxjpid = closest[0][2]
    for key, value in d.iteritems():
        if value > max:
            max = value
            maxjpid = key

  #  print maxjpid
    return maxjpid

def crossval(x):
    traj=[]
    jpids = []
    for line,jpid in zip(trainSet["Trajectory"],trainSet["journeyPatternId"]):
        traj.append(line)
        jpids.append(jpid)
    i = [k for k in range(0,len(traj))]
   # print i
    res=[]
    shuffle(i)
    ls=[]
    lm=int(len(traj)*0.01)

    for k in range(int(len(traj)*0.05)):
        ls.append([traj[i[k]],jpids[i[k]]])


    i=i[0:int(len(traj)*0.05)]

    for j in range(0,10):
        i = [k for k in range(0,len(traj))]
        shuffle(i)
        ls=[]
        lm=int(len(traj)*0.01)

        for k in range(int(len(traj)*0.1)):
            ls.append([traj[i[k]],jpids[i[k]]])


        i=i[0:int(len(traj)*0.1)]
        i = [k for k in range(len(ls))]
        shuffle(i)
        limit = int(len(ls)/15)
        limit = 10
        print limit
        test= []#[traj[k] for k in i[0:int((1/3)*len(traj))]]

        test_ids =[]# [jpids[k] for k in i[0:int((1/3)*len(traj))]]
        for k in range(limit):
            test.append(ls[i[k]])
          #  test_ids.append(jpids[k])
        #print test_ids
        train = []#[traj[k] for k in i[int((1/3)*len(traj)):]]
        train_ids =[]#[jpids[k] for k in i[int((1/3)*len(traj)):]] 
        for k in range(limit,len(i)):
            train.append(ls[i[k]])
            #train_ids.append(jpids[k])

       # train = [traj[k] for k in i[int((1/3)*len(traj)):]]
      #  train_ids =[jpids[k] for k in i[int((1/3)*len(traj)):]] 


        preds = []
        for route in test:
            lonlat=[]
            for x in route[0]:
                lonlat.append((x[1],x[2]))

            trajectory_list = []
            journey_list = []
            for x, jpid in train: #zip(train,train_ids):
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
            preds.append(knn(closest))

        correct = 0

        for k in range(0,len(test)):
            print test[k][1],"->",preds[k]
            if test[k][1] == preds[k]:
                correct+=1
        print correct
        res.append(correct/len(test))

    print "===========================",res
    return res







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
trainSet = pd.read_csv('./train_set.csv',converters={"Trajectory": literal_eval},index_col='tripId')
crossval(trainSet)

# read test set and make lon-lat lists
trajectory_list0 = []
predicts = []
with open('./test_set_a2.csv','rb') as csvfile:
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
    '''   gmap = gmplot.GoogleMapPlotter(lonlat[0][1],lonlat[0][0], 13)
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
    predicts.append(knn(closest))
    print "total_time : %s\n====================\n\n" %(total_time)'''


data = {'Test_Trip_ID' : [i for i in range(1,6)],
    'Predicted_JourneyPatternID' : [i for i in predicts]}

df = pd.DataFrame(data, columns = ['Test_Trip_ID','Predicted_JourneyPatternID'])

df.to_csv('./testSet_JourneyPatternIDs.csv', sep='\t', index=False)
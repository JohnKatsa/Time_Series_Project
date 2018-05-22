import pandas as pd
import numpy as np
from ast import literal_eval
import csv
from dtw import dtw

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
with open('./train_set.csv','rb') as csvfile:
    for row in csvfile:
        trajectory_list.append(row)
trajectory_list.pop(0)
trajectory_list = [literal_eval(x) for x in trajectory_list]

# get for each pair the dtw distances and store them in closest
for trip in trajectory_list:
    lonlattest = []
    closest = []
    index = 0
    for x in trip:
        lonlattest.append((x[1],x[2]))
    d = dtw(lonlat1,lonlattest,dist=harvesine)
    closest.append((index,d))
    index+=1

closest = np.asarray(closest)
minfive = arr.argsort()[:5]

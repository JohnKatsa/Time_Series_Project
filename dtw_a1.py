import pandas as pd
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
with open('./train_set_a1.csv','rb') as csvfile:
    for row in csvfile:
        trajectory_list.append(row)
trajectory_list.pop(0)
trajectory_list = [literal_eval(x) for x in trajectory_list]

# get for each pair the closest
for trip in trajectory_list:
    lonlattest = []
    closest = []
    for x in trip:
        lonlattest.append((x[1],x[2]))
    dtw(lonlat1,lonlattest,dist=harvesine)

print lon

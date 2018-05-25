import pandas as pd
from ast import literal_eval

import gmplot

trainSet = pd.read_csv(
'./train_set.csv', # replace with the correct path
converters={"Trajectory": literal_eval},
index_col='tripId',
nrows=1000
)

filenames = ["mymap1.html","mymap2.html","mymap3.html","mymap4.html","mymap5.html"]

fi = 0;

latlong = []

checklist = []

for i,jpid in zip(trainSet['Trajectory'],trainSet["journeyPatternId"]):        # for every journeypattern
    if jpid in checklist:
        continue;
    checklist.append(jpid)
    for j in i:
        latlong.append((j[2],j[1]))     # make list of latitudes and longtitudes
        #print latlong
    gmap = gmplot.GoogleMapPlotter(latlong[0][0], latlong[0][1], 13)
    lats, lons = zip(*latlong)
    gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
    # Draw
    gmap.draw(filenames[fi])
    fi += 1;
    latlong = []
    if fi == 5:
        break

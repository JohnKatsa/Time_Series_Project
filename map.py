import pandas as pd
from ast import literal_eval

import gmplot

trainSet = pd.read_csv(
'./train_set.csv', # replace with the correct path
converters={"Trajectory": literal_eval},
index_col='tripId'
)

filenames = ["my_map1.html","my_map2.html","my_map4.html","my_map5.html","my_map6.html"]
fi = 0;

latlong = []

for i in trainSet['Trajectory']:        # for every journeypattern
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

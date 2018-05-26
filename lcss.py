#LCSS
import pandas as pd
from ast import literal_eval
import time
from math import radians, cos, sin, asin, sqrt
import numpy as np
import gmplot

def cmp(x,y):
	if x[0] > y[0]:
			return -1
	elif x[0] == y[0]:
		return 0
	return 1
def haversine(x,y):
	"""
	Calculate the great circle distance between two points
	on the earth (specified in decimal degrees)
	"""
	# convert decimal degrees to radians
	lon1, lat1, lon2, lat2 = map(radians, [x[1], x[2], y[1], y[2]])

	# haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a))
	r = 6371 # Radius of earth in kilometers. Use 3956 for miles
	return c * r


# X and Y lists with m , n elements respectively
def lcss(X,Y):
	#C = [0] * (len(X) + len(Y))	# Initialize C with zeros
	C = [[0 for x in range(len(Y))] for y in range(len(X))] 

	for i in range(1,len(X)):
		for j in range(1,len(Y)):
			k=haversine(X[i],Y[j])
			
			#print k
			if k <= 0.2 :
				#print i,j
				C[i][j] = C[i-1][j-1] + 1
			else :
				if C[i][j-1] > C[i-1][j]:
					C[i][j] = C[i][j-1]
				else  :
					C[i][j] = C[i-1][j]

	return C
# Backtracks the C array to find a LCS
def backtrack(C,X,Y,i,j):
	l=[]
	if i==0 or j==0:
		return l
	if haversine(X[i],Y[j]) <= 0.2 :
		l=backtrack(C,X,Y,i-1,j-1)
		l.append(X[i])
		return l#backtrack(C,X,Y,i-1,j-1).append(X[i])
	if C[i][j-1] > C[i-1][j]:
		return backtrack(C,X,Y,i,j-1) 
	return backtrack(C,X,Y,i-1,j)



trainSet = pd.read_csv('./train_set.csv',converters={"Trajectory": literal_eval},index_col='tripId',nrows=1500)
trainSet = trainSet[0:1200]
trajectory_list = []
with open('./test_set_a2.csv','rb') as csvfile:
	for row in csvfile:
		trajectory_list.append(row)
trajectory_list.pop(0)
trajectory_list = [literal_eval(x) for x in trajectory_list]

print trainSet["journeyPatternId"][1]
start_time = time.time()


filenames = ["my_map1.html","my_map2.html","my_map4.html","my_map5.html","my_map6.html"]
fi=0
counter = 0
for route in trajectory_list:
	file = "original" + str(counter)+".html"
	latlong = []
	for j in route:
		latlong.append((j[2],j[1]))
	gmap = gmplot.GoogleMapPlotter(latlong[0][0], latlong[0][1], 13)
	lats, lons = zip(*latlong)
	gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
	gmap.draw(file)

	cm=[]
	for line,jpid in zip(trainSet["Trajectory"],trainSet["journeyPatternId"]):
		C = lcss(route,line)
		print C[len(route)-1][len(line)-1]
		cm.append([C[len(route)-1][len(line)-1],backtrack(C,route,line,len(route)-1,len(line)-1),jpid,route])
	cm.sort(cmp=cmp)
	latlong = []
	latsl = []
	fi=0
	for i in range(0,5):
	   #print cm[i][2:]
		latlong = []
		latsl = []
		file = "map" + str(counter)+ "_"+str(fi)+".html"
		for j in cm[i][3]:
			latlong.append((j[2],j[1]))
		for jj in cm[i][1]:
			latsl.append((jj[2],jj[1]))

		gmap = gmplot.GoogleMapPlotter(latlong[i][0], latlong[i][1], 13)
		lats, lons = zip(*latlong)
		gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
		
		if len(cm[i][1]) > 0:
			#gmap = gmplot.GoogleMapPlotter(latsl[0][0], latsl[0][1], 19)
			lats2, lons2 = zip(*latsl)
			gmap.plot(lats2,lons2,'red',edge_width=6)
		gmap.draw(file)
		fi += 1
		#print fi,i
		if fi >= 5:
			break
	counter+=1
	total_time = time.time()-start_time#  time.time()
print "total_time:",total_time


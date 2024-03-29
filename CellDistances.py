# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:58:56 2024

@author: aaquiles
"""

######         MEASURE METRICS TO TRAIN THE RF algorithm      #########

#### FOUND THE CENTROID AND MEASURE THE DISTANCES

Im_here =  [round(np.mean(X),2),round(np.mean(Y),2)]                             # recommended to put a centroid here  (mean)
My_coord = np.vstack((X,Y)).T

def calculateDistance (Im_here, you_there):
    x1,y1 = Im_here
    x2,y2 = you_there
    for i in you_there:
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist

Distances = []
for i in range(0, len(My_coord)):
    Distances.append(calculateDistance(Im_here,My_coord[i]))
    
Distances = np.array(Distances)

##### Full scatter colored by distance 
plt.figure(0)
plt.scatter(X,Y, s=200, c = Distances, cmap = 'jet')
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
##### test a scatter colored by distance in every Cluster
CtCells = Ctrl['Liste Cellules']
Test = CtCells[0]
lst_int = np.array([int(x) for x in Test.split(",")])
plt.figure(1)
plt.scatter(X[lst_int], Y[lst_int], s = 200, c= Distances[lst_int], cmap = 'jet',
            vmin = 0, vmax = 300)
# plt.colorbar()
plt.grid(False)
plt.xlim(50,500)
plt.ylim(50,500)
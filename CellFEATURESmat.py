# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:14:39 2024

@author: aaquiles
"""

###                   For all the clusters run :

def ClassCLusterData (Entrance, Dist, n,c1, c2, S, O):
    
    Test = Entrance
    lst_int = np.array([int(x) for x in Test.split(",")])
    lst_int =   lst_int - 1
    DistInt = Dist[lst_int]
    Clust = np.vstack((lst_int,DistInt)).T
    Class = pd.DataFrame(Clust, columns = ["ID","Distances"])
    Class['Cluster'] = f'Clust{n}'
    
    x = c1[lst_int]
    y = c2[lst_int]
    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
   
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
   
    Area = math.pi*ell_radius_y*ell_radius_x 
    Class['Ellipse'] = ell_radius_y
    Class['Area'] = Area
    Class['Size'] = S[n]
    Class['Freq'] = O[n]

    return Class                                                                # Returns an array With cell ID, Distance, Number of Cluster, Ellipse Lenght, Area


CtCells = pd.DataFrame(Ctrl[['Liste Cellules', 'Nbre Cellules Groupe', 'Occurence Groupe']])  ## Choose the data file
CtCells['ID'] = np.arange(0,len(CtCells),1)
CtCells = CtCells.set_index('ID')

Size = CtCells['Nbre Cellules Groupe']
Ocu = CtCells['Occurence Groupe']
CtCells = CtCells['Liste Cellules']

ClassMat = []

for i in range(0, len(CtCells)):
    ClassMat.append(ClassCLusterData(CtCells[i],Distances,i, X,Y, Size, Ocu))

ClassMAT = pd.concat(ClassMat)
ClassMATv = ClassMAT.drop('ID', axis = 1)
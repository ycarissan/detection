import numpy as np 
import matplotlib.pyplot as plt
#naphtalene.xyz
print("---------------------detection--------------------------")

filename = "naphtalene.xyz"
atoms = []
coordinates = []
xyz = open(filename)
n_atoms = int(xyz.readline())
title = xyz.readline()
for line in xyz:
    atom,x,y,z = line.split()
    atoms.append(atom)
    coordinates.append([float(x), float(y), float(z)])
xyz.close()

print("filename:         %s" % filename)
print("title:            %s" % title)
print("number of atoms:  %d" % n_atoms)


print(atoms)
#print(coordinates)

coordinates2 = coordinates
#creation of a hydrogen atoms list and a carbon atoms list 
#after a function will be coded 
hList = []
cList = []
for i in range(len(atoms)):
    if atoms[i]=="H":
        hList.append(coordinates[i])
    else:
        cList.append(coordinates[i])
print(cList)
#print(hList)
"""def read_xyz(filename): 
   Read filename in XYZ format and return lists of atoms and coordinates.

   If number of coordinates do not agree with the statd number in
   the file it will raise a ValueError.
   

   atoms = []
   coordinates = []

   xyz = open(filename)
   n_atoms = int(xyz.readline())
   title = xyz.readline()
   for line in xyz:
       atom,x,y,z = line.split()
       atoms.append(atom)
       coordinates.append([float(x), float(y), float(z)])
   xyz.close()

   if n_atoms != len(coordinates):
      raise ValueError("File says %d atoms but read %d points." % (n_atoms, len(coordinates))

   return atoms, coordinates
print(read_xyz(naphtalene.xyz))"""  #ne marche pas 
#YC
"""print(read_xyz('naphtalene.xyz'))"""  #devrait marcher
#YC
v2=[]
v3=[]
d1=0
d2=0
d3=0
neighbor=[]
notneighbor=[]
k=0

# Je ne comprends pas ce que ça fait:
# Je comprends que les boucles sur i et j cherchent qui est voisin de qui mais les autres, je ne sais pas.
# À mon avis il faut d'abord faire la liste des voisins, puis la traiter au lieu de vouloir tout faire en même temps.
# Mon algo serait
# faire la liste des premiers voisins
# faire une boucle sur tous les atomes:
#   si un atome a 2 voisins qui portent chacun un hydrogène, alors c'est un site que je recherche
#   donc je calcule le barycentre
for i in range(0,len(cList)):
    for j in range(i,len(cList)): #c'est quand je met cette range que cela ne trouve rien, j'ai essayé avec range(1,len(cList)), mais je trouve des résultats incohérents
        v1=[coordinates[i][0]-coordinates[j][0],coordinates[i][1]-coordinates[j][1]] 
        d1=np.linalg.norm(v1) #ici test voisinage coordinates[i] et coordinates[j]
        if d1<=2 and d1!=0:
            for v in range(j,len(cList)):
                v2=[coordinates[i][0]-coordinates[v][0],coordinates[i][1]-coordinates[v][1]]  
                d2=np.linalg.norm(v2) # ici test voisinage entre coordinates[i] et coordinates[v]
                if d2<=2 and d2!=0:
                    v3=[coordinates[j][0]-coordinates[v][0],coordinates[j][1]-coordinates[v][1]]
                    d3=np.linalg.norm(v3) # ici test voisinage entre coordinates[j] et coordinates[v]
                    L=[coordinates[i],coordinates[j],coordinates[v]]
                    if d3<=2.5 and d3!=0:  #j'ai mis 2.5 car à la main je trouvais 2.5
                        neighbor.append(L)
                        k=k+1
                    print("i : ",i," j : ",j," v : ",v) # pour comprendre mon erreur """




print(" ")
print(" ")
#print(neighbor, "------------------",k) #k= number of carbon atoms in zig-zag 
print(" ")
print(" ")
#print(neighbor[1],"         ",neighbor[2],"       ", neighbor[3])

i=0
for i in range(len(neighbor)):
    print(neighbor[i])

print(" ")
print(k)
x=[]
y=[]
print(neighbor)
for i in range(len(neighbor)):
    for j in range(len(neighbor[i])):
        x.append(neighbor[i][j][0])
        y.append(neighbor[i][j][1])
print("x  et  y")

print(x)
print(y)
plt.scatter(x, y)
plt.show()
a=[]
b=[]
for i in range(len(cList)):
    a.append(cList[i][0])
    b.append(cList[i][1])

plt.scatter(a,b)
plt.show()
print("---------------------fin detection--------------------------")

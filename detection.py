import numpy as np 
import matplotlib.pyplot as plt
#naphtalene.xyz
print("---------------------detection--------------------------")
atoms = []
coordinates = []
cList = []
hList = []
v1=[]
d1=0
neighbor=[]
M=[]
k=0

def read_xyz(filename): 
    # RL
    # à la base je voulais faire des sous-programmes qui s'appelaient entre eux mais je suis assez rouillé dans cette notion de python, du coup j'ai fait tout dans un
    # je vais me renseigner plus sur cela 
    # pour l'instant j'ai fait la liste des carbones voisins, je préfère vous demander si c'est bon avant de passez aux hydrogènes
    # RL

    xyz = open(filename)
    n_atoms = int(xyz.readline())
    title = xyz.readline()
    for line in xyz:
        atom,x,y,z = line.split()
        atoms.append(atom)
        coordinates.append([float(x), float(y), float(z)])
    xyz.close()

    if n_atoms != len(coordinates):
        raise ValueError("File says %d atoms but read %d points." % (n_atoms, len(coordinates)))

def selectAtoms(L):
    for k in range(len(L)):
        if L[k]=='H':
            hList.append(coordinates[k])
        else:
            cList.append(coordinates[k])
    

def voisin(L):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            v1=[coordinates[i][0]-coordinates[j][0],coordinates[i][1],coordinates[j][1]]
            d1=np.linalg.norm(v1)
            if d1<=2 and d1!=0:
                M=[coordinates[i],coordinates[j]]
                neighbor.append(M)
    for i in range(len(neighbor)):
        print(neighbor[i])
def scatter(L):
    x=[]
    y=[]
    for i in range(len(L)):
        for j in range(len(L[i])):
            x.append(L[i][j][0])
            y.append(L[i][j][1])
    plt.scatter(x,y)
    plt.show()



read_xyz("naphtalene.xyz")
selectAtoms(atoms)
voisin(cList)
scatter(neighbor)
print()
print(neighbor)
print("---------------------fin detection--------------------------")

#YC

# Je ne comprends pas ce que ça fait:
# Je comprends que les boucles sur i et j cherchent qui est voisin de qui mais les autres, je ne sais pas.
# À mon avis il faut d'abord faire la liste des voisins, puis la traiter au lieu de vouloir tout faire en même temps.
# Mon algo serait
# faire la liste des premiers voisins                           # RL : j'ai essayé de faire cela pour  l'instant 
# faire une boucle sur tous les atomes:
#   si un atome a 2 voisins qui portent chacun un hydrogène, alors c'est un site que je recherche
#   donc je calcule le barycentre

"""for i in range(len(cList)):
    for j in range(i+1, len(cList)):
        v1=[coordinates[i][0]-coordinates[j][0],coordinates[i][1],coordinates[j][1]]
        d1=np.linalg.norm(v1)
        if d1<=2 and d1!=0:
            M=[coordinates[i],coordinates[j]]
            neighbor.append(M)"""

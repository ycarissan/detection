import numpy as np 
import matplotlib.pyplot as plt
import molecule as mol

# 1/ J'ai refactorisé le programme en faisant un programme principal (ci-dessous) et en faisant les modifications suivantes
# 2/ Pour les variables, de mon poitn de vue, il vaut mieux garder uniquement les variables les plus importantes
# comme globales le reste, on les definit à la volée
# 3/ Je propose de créer une classe molecule (une sorte d'équivalent d'un objet) pour conserver tout ce qui concerne une
# molecule: lire un fichier xyz, écrire un fichier xyz, trouiver les voisins, etc.
# 4/ J'ai mis cette classe dans un fichier à part
def main():
    print("---------------------detection--------------------------")

    molecule = mol.Molecule("naphtalene.xyz")
    print()
    print(molecule.neighbor)
    print()
    print("liste carbon voisin hydrogène : ", molecule.neighborHydrogen)
    print()
    print("cList : ", molecule.cList)
    print()
    print("hList : ", molecule.hList)
    print()
    print("liste carbones voisin hydrogène : ", molecule.neighborHydrogen)
    molecule.scatter(molecule.neighbor)
   
    print("---------------------fin detection--------------------------")

if __name__=="__main__":
    print("Appel en tant que programme principal")
    main()

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

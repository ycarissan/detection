import numpy as np 
import matplotlib.pyplot as plt

class Molecule:
    def __init__(self, filename):
        self.atoms = []
        self.coordinates = []
        self.cList = []
        self.hList = []
        self.neighbor=[]
        self.read_xyz(filename)
        self.selectAtoms(self.atoms)
        self.voisin(self.cList)

    def read_xyz(self, filename): 
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
            self.atoms.append(atom)
            self.coordinates.append([float(x), float(y), float(z)])
        xyz.close()
    
        if n_atoms != len(self.coordinates):
            raise ValueError("File says %d atoms but read %d points." % (n_atoms, len(coordinates)))
    
    def selectAtoms(self, L):
        for k in range(len(L)):
            if L[k]=='H':
                self.hList.append(self.coordinates[k])
            else:
                self.cList.append(self.coordinates[k])
        
    def voisin(self, L):
        """
        Génère la liste des voisins pour chaque atome de carbone
        """
        for i in range(len(L)):
            for j in range(i+1, len(L)):
                v1=[self.coordinates[i][0]-self.coordinates[j][0],self.coordinates[i][1],self.coordinates[j][1]]
                d1=np.linalg.norm(v1)
                if d1<=2 and d1!=0:
                    M=[self.coordinates[i],self.coordinates[j]]
                    self.neighbor.append(M)
        for i in range(len(self.neighbor)):
            print(self.neighbor[i])

    def scatter(self, L):
        """
        Affiche les points contenus dans la liste passee en argument
        """
        x=[]
        y=[]
        for i in range(len(L)):
            for j in range(len(L[i])):
                x.append(L[i][j][0])
                y.append(L[i][j][1])
        plt.scatter(x,y)
        plt.show()

# 1/ J'ai refactorisé le programme en faisant un programme principal (ci-dessous) et en faisant les modifications suivantes
# 2/ Pour les variables, de mon poitn de vue, il vaut mieux garder uniquement les variables les plus importantes
# comme globales le reste, on les definit à la volée
# 3/ Je propose de créer une classe molecule (une sorte d'équivalent d'un objet) pour conserver tout ce qui concerne une
# molecule: lire un fichier xyz, écrire un fichier xyz, trouiver les voisins, etc.
# 4/ Par la suite, on poourra mettre tout ça dans un fichier a part
def main():
    print("---------------------detection--------------------------")

    molecule = Molecule("naphtalene.xyz")
    molecule.scatter(molecule.neighbor)
    print()
    print(molecule.neighbor)
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

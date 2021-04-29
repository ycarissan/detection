import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import colorsys
import seaborn

def read_xyz(filename): 
    # RL
    # à la base je voulais faire des sous-programmes qui s'appelaient entre eux mais je suis assez rouillé dans cette notion de python, du coup j'ai fait tout dans un
    # je vais me renseigner plus sur cela 
    # pour l'instant j'ai fait la liste des carbones voisins, je préfère vous demander si c'est bon avant de passez aux hydrogènes
    # RL
    atoms=[]
    coordinates=[]
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
    return atoms, coordinates
    
class Molecule:
    def __init__(self, filename):
        self.cList = []
        self.hList = []
        self.neighbor=[]
        self.neighborHydrogen=[]
        self.atoms, self.coordinates = read_xyz(filename)
        self.selectAtoms(self.atoms)
        self.voisin(self.cList)
        self.zig_zag(self.cList, self.hList)

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
        mark = [".",",","o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_",0,1,2,3,4,5,6,7,8,9,10,11]
        for i in range(0,len(L)):
            plt.scatter(L[i][0][0],L[i][0][1],c='b',marker=mark[i])
            plt.scatter(L[i][1][0],L[i][1][1],c='b',marker=mark[i])

            """for j in range(len(L[i])):
                x.append(L[i][j][0])
                y.append(L[i][j][1])
                plt.scatter(x,y)
            #plt.scatter(L[i+1][j][0],L[i+1][j][1])"""
                
        #plt.scatter(x,y)
        plt.show()
    def zig_zag(self,M,L):
        v=[]
        d=0
        for i in range(len(M)):
            for j in range(len(L)):
                v=[M[i][0]-L[j][0],M[i][1]-L[j][1]]
                d=np.linalg.norm(v)
                if d<=2 and d!=0:
                    self.neighborHydrogen.append(M[i])



        
                                              
    


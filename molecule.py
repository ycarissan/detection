import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import colorsys
import seaborn
import atome

def read_xyz(filename): 
    # RL
    # à la base je voulais faire des sous-programmes qui s'appelaient entre eux mais je suis assez rouillé dans cette notion de python, du coup j'ai fait tout dans un
    # je vais me renseigner plus sur cela 
    # pour l'instant j'ai fait la liste des carbones voisins, je préfère vous demander si c'est bon avant de passez aux hydrogènes
    # RL
    atomlist=[]
    xyz = open(filename)
    n_atoms = int(xyz.readline())
    title = xyz.readline()
    for line in xyz:
        atom,x,y,z = line.split()
        atomlist.append(atome.Atome(atom, float(x), float(y), float(z)))
    xyz.close()

    if n_atoms != len(atomlist):
        raise ValueError("File says %d atoms but read %d points." % (n_atoms, len(atomlist)))
    return atomlist
    
class Molecule:
    def __init__(self, filename):
        self.neighbour = []
        self.atomlist = read_xyz(filename)
        self.voisin()
        self.printVoisins()
        self.zigzag = self.zig_zag()

    """
    Pour chaque atom de carbone, on fait une liste de voisins
    QUI DEBUTE PAR L'ATOME CONSIDERE
    Donc un atome a 3 voisins aura une liste de taille 4:
    lui-même puis les 3 voisins quel que soit leur type
    """
    def voisin(self):
        """
        Génère la liste des voisins pour chaque atome de carbone
        """
        for at1 in self.atomlist:
            if at1.getlabel() == 'C':
                pos1 = np.array(at1.getCoords())
                voisins_1 = []
                voisins_1.append(at1)
                for at2 in self.atomlist:
                    pos2 = np.array(at2.getCoords())
                    V12 = pos2 - pos1
                    dist =  np.linalg.norm(V12)
                    if (dist > 1e-6) and (dist < 2):
                        voisins_1.append(at2)
                self.neighbour.append(voisins_1)

    def printVoisins(self):
        for el in self.neighbour:
            print("Voisins de {} :".format(el[0]))
            for at in el:
                at.print()

#          for i in range(len(L)):
#  #            for j in range(i+1, len(L)):
#  # ici il y a un problème.
#  #prenons le cas où 2 est voision de 1 et 3 cet algorithme teste le voisinage de 2 avec 3 mais pas de 3 avec 2 car 3>2
#  # on peut donc faire:
#              for j in range(len(L)):
#                  if (i!=j) :
#                      v1=[self.coordinates[i][0]-self.coordinates[j][0],self.coordinates[i][1],self.coordinates[j][1]]
#                      d1=np.linalg.norm(v1)
#                      if d1<=2 and d1!=0:
#                          M=[self.coordinates[i],self.coordinates[j]]
#                          self.neighbor.append(M)
#          for i in range(len(self.neighbor)):
#              print(self.neighbor[i])

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

    """
    Renvoit la liste des carbones ayant 3 voisins carbone
    """
    def zig_zag(self):
        v=[]
        for el in self.neighbour:
            at0 = el[0]
            store=True
            for i in range(1,3):
                print('lbl'+el[i].getlabel())
                if el[i].getlabel() == 'H':
                    store=False
            if store:
                v.append(el)
        return v
#
#
#
#
#        d=0
#        for i in range(len(M)):
#            for j in range(len(L)):
#                v=[M[i][0]-L[j][0],M[i][1]-L[j][1]]
#                d=np.linalg.norm(v)
#                if d<=2 and d!=0:
#                    self.neighborHydrogen.append(M[i])



       
                                              
    


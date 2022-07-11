import numpy as np
inf = float('inf')



def init(départ, nb_villes):
    # la fonction initialise la liste VILLES
    # à partir de départ (int)
    # nb_villes est le nombre de villes dans le graphe
    VILLES=[]   # initialisation de la liste VILLES
    for i in range(nb_villes):
        if i==départ:
            VILLES.append([-1, 0, True])
           # la valeur -1 n'est pas utilisée car ville de départ
           # True : uniquement la ville de départ est sélectionnée
        else:
            VILLES.append([-1, inf, False])
           # la valeur -1 n'est pas utilisée car distance infinie
           # False : ville non sélectionnée
    return VILLES

def dijkstra(M, départ, arrivée):
    # la fonction permet d'avoir le plus court chemin
    # de départ (int) à arrivée (int) dans la liste L à partir
    # de la matrice d'adjacence M. On récupère la liste VILLES
    nb_villes=np.shape(M)[0] # nb de villes = nb de lignes de M
    VILLES=init(départ, nb_villes) # initialisation de la
                                   # liste VILLES
    # l'algorithme est appliqué pour la ville position
    position=départ
    while (position!=arrivée):
        indice=position
        for i in range(nb_villes):   # i décrit toutes les villes
            if VILLES[i][2]==False : # ville non sélectionnée
                somme=VILLES[position][1]+M[position, i]
                if somme<VILLES[i][1]:
                    VILLES[i][1]=somme
                       # nouvelle valeur de la distance à
                       # la ville de départ
                    VILLES[i][0]=position # nouvelle ville
                                        # précédente sur le chemin
        # recherche du minimum des distances pour les villes
        # non sélectionnées
        val_min=inf
        for i in range(nb_villes):
            if VILLES[i][2]==False and VILLES[i][1]<val_min:
                indice=i
                val_min=VILLES[i][1]
        if indice==position:
            return [],inf           # on n'atteint pas arrivée
        else:
            VILLES[indice][2]=True  # cette ville est sélectionnée
            position=indice  # nouvelle valeur de la variable
                             # position
 
    # liste des villes parcourues
    i=arrivée
    L=[arrivée]  # L = liste des villes parcourues en sens inverse
    while (i!=départ):
        i=VILLES[i][0]
        L.append(i)
    L.reverse()  # il faut inverser la liste L pour obtenir la
                 # liste des villes parcourues dans le sens direct
    return L, VILLES[arrivée][1]

# initialisation du programme
    #Matrice D'adjacence
M=np.array([[0, 13, 29, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
 	    [13, 0, 17, 59, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
 	    [29, 17, 0,  42, 73, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, 59, 42, 0, 63, 24, inf, inf, inf, inf, inf, inf, inf, inf, inf, 65, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
        [inf, inf, 73, 63, 0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 64, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, 24, inf, 0, 63, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, 63, 0, 38, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, 38, 0, 130, 74, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, 130, 0, inf, inf, inf, 225, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
        [inf, inf, inf, inf, inf, inf, inf, 74, inf, 0, 128, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, 128, 0, 79, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 79, 0, 240, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, 225, inf, inf, 240, 0, 135, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 135, 0, 249, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 249, 0, inf, inf, inf, inf, inf, inf, inf, inf, inf, 95, inf, inf, inf, inf, 129, 234],
	    [inf, inf, inf, 65, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 42, 25, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, 64, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 42, 0, 46, 27, 46, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 25, 46, 0, 27, inf, inf, inf, inf, inf, inf, inf, inf, 125, 41, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 27, 27, 0, 39, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 46, inf, 39, 0, inf, inf, inf, inf, inf, inf, inf, 65, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 59, 0, 45, inf, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 45, 0, 123, inf, inf, inf, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 123, 0, 33, inf, inf, 85, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 33, 0, inf, 186, inf, inf, inf, inf, inf],
        [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 95, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 102, inf, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 186, 102, 0, 91, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 85, inf, inf, 91, 0, inf, inf, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 125, inf, 65, inf, inf, inf, inf, inf, inf, inf, 0, 109, 85, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, 122, inf, inf, inf, inf, inf, inf, inf, inf, 41, inf, inf, inf, inf, inf, inf, inf, inf, inf, 109, 0, inf, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 129, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 85, inf, 0, inf],
	    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 234, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0],
])

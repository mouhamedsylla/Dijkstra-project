from Dijkstra_V3 import *
import webbrowser
from Coordonnees import *
import folium
from folium import plugins
from mesdistances import *
from Villes import *
print("""
████████▄   ▄█       ▄█    ▄█   ▄█▄    ▄████████     ███        ▄████████    ▄████████        ▄████████  ▄██████▄     ▄████████ ████████▄     ▄████████ 
███   ▀███ ███      ███   ███ ▄███▀   ███    ███ ▀█████████▄   ███    ███   ███    ███       ███    ███ ███    ███   ███    ███ ███   ▀███   ███    ███ 
███    ███ ███▌     ███   ███▐██▀     ███    █▀     ▀███▀▀██   ███    ███   ███    ███       ███    ███ ███    ███   ███    ███ ███    ███   ███    █▀  
███    ███ ███▌     ███  ▄█████▀      ███            ███   ▀  ▄███▄▄▄▄██▀   ███    ███      ▄███▄▄▄▄██▀ ███    ███   ███    ███ ███    ███   ███        
███    ███ ███▌     ███ ▀▀█████▄    ▀███████████     ███     ▀▀███▀▀▀▀▀   ▀███████████     ▀▀███▀▀▀▀▀   ███    ███ ▀███████████ ███    ███ ▀███████████ 
███    ███ ███      ███   ███▐██▄            ███     ███     ▀███████████   ███    ███     ▀███████████ ███    ███   ███    ███ ███    ███          ███ 
███   ▄███ ███      ███   ███ ▀███▄    ▄█    ███     ███       ███    ███   ███    ███       ███    ███ ███    ███   ███    ███ ███   ▄███    ▄█    ███ 
████████▀  █▀   █▄ ▄███   ███   ▀█▀  ▄████████▀     ▄████▀     ███    ███   ███    █▀        ███    ███  ▀██████▀    ███    █▀  ████████▀   ▄████████▀  
                ▀▀▀▀▀▀    ▀                                    ███    ███                    ███    ███                                                 
                                                                                          
 """)

print()
print()
print()
print("************************************************************************************************************************************************")
# Entré et controle de saisi
starting = ""
ending = ""
cond = False
cond1 = False
while cond == False:
    starting = input("Entrer votre ville de départ : ")
    for l in Coord:
        if l.lower() == starting.lower():
            starting = l
    try:
        if starting == "" or starting not in Coord:
            cond = False
            cond / 0 
        else:
            cond = True
    except:
        if cond == False:
            print("Error !!! Veillez entrez une ville valide")
            print()
while cond1 == False:
    ending = input("Entrer votre destination : " )
    for k in Coord:
        if k.lower() == ending.lower():
            ending = k
    for i in Coord:
        if i.lower == ending.lower():
            ending = i
    try:
        if ending == "" or ending not in Coord:
            cond1 = False
            cond / 0
        else:
            cond1 = True
    except:
        if cond1 == False:
            print("Error !!! Veillez entrez une ville valide")
            print()

# Chercher les numéros correspondant aux de départ et d'arrivée
def cherche_ville(ville):
    for i in range(0, 31):
        if ville == Villes[i]:
            return i

départ = cherche_ville(starting)
arrivée = cherche_ville(ending)

# Tester les voies empruntrer aller-retour et déterminer le chemin optimal
def cherche_court_chemin(dep, arr):
    r, d = dijkstra(M, dep, arr)
    r1, d1 = dijkstra(M, arr, dep)
    diste = [d, d1]
    a = min(diste)
    if a == d:
        L = r
    else:
        L = r1
    return a, L

dist, liste = cherche_court_chemin(départ, arrivée)
# Reconstruire notre itineraire
itineraire = []
for i in liste:
    itineraire.append(Villes[i])

if itineraire[0] == ending:
    roads = " ----> ".join(itineraire[::-1])
    print(roads)
else:
    roads = " ----> ".join(itineraire)
    print(roads)
print ("Distance parcourue = ", dist)

# Création de notre carte
m = folium.Map(location=[14.814349, -17.249890], zoom_start=15)
route = []
for i in itineraire:
    loc = Coord[i]
    marker = folium.Marker(location=loc, popup=i)
    marker.add_to(m)
    route.append(Coord[i])
plugins.AntPath(route).add_to(m)

m.save("C:\\Users\\HP\\Desktop\\Projet Dijkstra Roads\\roads.html")
url = 'C:\\Users\\HP\\Desktop\\Projet Dijkstra Roads\\roads.html'
webbrowser.open_new_tab(url)
print("************************************************************************************************************************************************")

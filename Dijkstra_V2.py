import math
"""
nodes - dictionnaire {sommet  : {successeur : poids}}
"""


nodes = {
    'Dakar' : {'Pikine' : 13.2,
               'Rufisque' : 29.4},
    'Pikine' : {#'Guediawaye' : 2.9,
                'Rufisque' : 17.5,
                'Thies' : 59.7},
    'Rufisque' : {'Thies' : 42.6,
                 'Mbour' : 73.2},
    'Thies' : {'Tivaoune' : 24.2,
               'Mbour' : 63,
               'Bambey' : 65.1,
               'Mbacké': 123},
    'Tivaoune' : {'Kébémer' : 63,
                  'Mbacké' : 116},
    'Mbour' : {'Fatick' : 64.2},
    'Bambey' : {'Diourbel' : 25.1,
                'Fatick' : 42.3},
    'Kébémer' : {'Louga' : 37.7,
                 'Mbacké' : 101,},
    'Diourbel' : {'Mbacké' : 40.7,
                 'Fatick' : 46.1,
                 'Gossas' : 27.6},
    'Fatick' : {'Gossas' : 49.9,
                'Kaolack' : 45.8,
                #'Foundiougne' : 27.2
                },
    'Gossas' : {'Guinguinéo' : 35.8},
    'Guinguinéo' : {'Birkilane' : 56},
    'Birkilane' : {'Kaffrine' : 24},
    'Kaolack' : {'Guinguinéo': 26.6,
                 #'Foundiougne' : 66.4,
                 'Nioro du Rip' : 59.1,
                },
    'Foundiougne' : {'Kaolack' : 66},
    'Nioro du Rip' : {#'Soma' : 45.1,
                      'Bignona' : 168},
    'Soma' : {'Bignona' : 123},
    'Kaffrine' : {'Malem Hodar' : 30.5},
    'Malem Hodar' : {'Koungheul' : 84.6},
    'Koungheul' : {'Koumpentoum' : 32},
    'Koumpentoum' : {'Tambacounda' : 133},
    'Louga' : {'Saint-Lious' : 74,
               'Linguère' : 130,
               'Mbacké' : 113},
    'Mbacké' : {'Linguère' : 122,
                'Kaffrine' : 109},
    'Linguère' : {'Ranérou' : 132,
                  'Matam' : 225},
    'Ranérou' : {'Matam' : 93.4,
                 'Bakel' : 230},
    'Saint-Lious' : {'Dagana' : 128},
    'Dagana' : {#'Podor' : 78.7,
                 'Matam' : 292},
    'Matam' : {'Bakel' : 164},
    'Bakel' : {'Goudiry' : 135},
    #'Goudiry' : {'Tambacounda' : 115},
    'Tambacounda' : {'Kédougou' : 234,
                     'Vélingara' : 95.1,
                     'Matam' : 242
                    },
    'Kédougou' : {'Salémata' : 78.8,
                  'Saraya' : 59.8},
    'Koumpentoum' : {'Koungheul' : 32.4,
                     'Tambacounda' : 102},
    'Vélingara' : {'Kolda' : 102,
                   #'Tambacounda' : 95
                    },
    #'Médina Yoro Foulah' : {'Kolda' : 95.7},
    'Kolda' : {'Sédhiou' : 90.7, 
               #'Vélingara' : 102
               },
    #'Sédhiou' : {#'Bignona' : 85.6,
                 #'Kolda' : 90.7},
    'Bignona' : {'Ziguinchor' : 33.4},
    'Ziguinchor' : {'Kolda' : 186
                  #  'Bignona' : 33.4
                    },

}

def dijkstra(dep, arr):
    itineraire_1 = []
    itineraire = []
    itineraire.append(dep)
    itineraire_1.append(dep)
    distance =  0 #s_dep[dep][0]
    actual_nodes = {}
    next_nodes = ""
    cpt = 0
    while itineraire[-1] != arr:
        poids = []
        for i in nodes:
            if i == dep:
                actual_nodes = i
                next_nodes = nodes[actual_nodes]
                break
            if next_nodes == dep:
                break    
        for j in next_nodes.items():
            poids.append(j[1])
        """if len(poids) < 2:
            break
        if poids == []:
            del nodes[actual_nodes]
        else:"""
        m = min(poids)
        if m != math.inf:
            distance += m
        for k in next_nodes.items():
            if k[0] == arr:
                next = k[0]
                m = k[1]
                for i in nodes:
                    for k in nodes[i].keys():
                        if k == next:
                            nodes[i][k] = math.inf
            elif k[1] == m:
                next = k[0]
                for i in nodes:
                    for k in nodes[i].keys():
                        if k == next:
                            nodes[i][k] = math.inf
        if next == dep:
            break
        itineraire.append(next)
        print("Nouveau noeud : "+next)
        #print(nodes)
        itineraire_1.append(next)
        dep = next


    print("distance = "+str(distance))

    print(itineraire_1)
    #print(distance)

    return distance, itineraire_1




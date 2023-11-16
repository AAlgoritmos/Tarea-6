#######################################################################
#                     Análisis de Algoritmos                          #
#                            Taller 4                                 #
#               María Catalina Ibáñez y Felipe Florian                #
#######################################################################

import random as rng
import pandas as pd
from random import randint
import networkx as nx

def generate(V, E):

    vertex = [i for i in range(V)]
    edges = []
    all_edges = []

    for a in range(V):
            for b in range(a, V):
                if a != b:
                    all_edges.append((a,b))
                      
    count = 0
    
    while count != E:
            e = rng.choice(all_edges)
            all_edges.remove(e)
            count += 1
            edges.append(e)


    return edges









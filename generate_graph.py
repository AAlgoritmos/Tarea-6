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

    while len(edges) < E:
        u = rng.choice(vertex)
        v = rng.choice(vertex)
        while v == u:
            v = rng.choice(vertex)
        if (u, v) not in edges or (v, u) not in edges:
            edges.append((u, v))

    return edges

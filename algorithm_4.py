from graph import SimpleGraph
import random

""" 
Escoger aleatoriamente un eje, incluir aleatoriamente uno de los dos vértices 
conectados, descartar todos los demás ejes conectados por el vértice escogido 
y repetir hasta que no queden ejes.
"""


def vertex_cover_4(G: SimpleGraph):
    """
    Returns a vertex cover of the graph.
    """
    cover = set()
    E = G.E.copy()
    while E:
        u, v = random.choice(E)
        vertex = random.choice([u, v])
        cover.add(vertex)
        E = [e for e in E if vertex not in e]

    return cover

from graph import SimpleGraph

"""
Escoger el vértice de mayor grado, descartar los ejes que llegan al vertice 
escogido y repetir hasta que no queden ejes.
"""


def vertex_cover_2(G: SimpleGraph):
    """
    Returns a vertex cover of the graph.
    """
    cover = set()
    E = G.E
    while E:
        u = max(G.V, key=G.degree)
        cover.add(u)
        G.V.remove(u)
        E = [e for e in E if u not in e]
    return cover

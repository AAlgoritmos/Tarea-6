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
    while G.E:
        u = max(G.V, key=G.degree)
        cover.add(u)
        G.V.remove(u)
        G.E = [e for e in G.E if u not in e]
    return cover

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
    G2 = G
    while G2.E:
        u = max(G2.V, key=G2.degree)
        cover.add(u)
        G2.V.remove(u)
        G2.E = [e for e in G2.E if u not in e]
    return cover

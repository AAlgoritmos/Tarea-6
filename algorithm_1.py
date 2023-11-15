from graph import SimpleGraph

"""
Escoger arbitrariamente un eje, incluir los dos vértices conectados, 
descartar todos los demás ejes conectados por los vertices escogidos 
y repetir hasta que no queden ejes.
"""


def vertex_cover_1(G: SimpleGraph):
    """
    Returns a vertex cover of the graph.
    """
    cover = set()
    E = G.E.copy()
    while E:
        u, v = E.pop()
        cover.add(u)
        cover.add(v)
        E = [e for e in E if u not in e and v not in e]
    return cover

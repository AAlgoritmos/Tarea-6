from graph import SimpleGraph

"""
Escoger arbitrariamente un eje, incluir el vértice de mayor grado de los dos vértices 
conectados por el eje, descartar todos los demás ejes conectados por el vértice escogido 
y repetir hasta que no queden ejes.
"""


def vertex_cover_3(G: SimpleGraph):
    """
    Returns a vertex cover of the graph.
    """
    cover = set()
    E = G.E.copy()
    while E:
        u, v = E.pop()
        if G.degree(u) > G.degree(v):
            cover.add(u)
            E = [e for e in E if u not in e]
        else:
            cover.add(v)
            E = [e for e in E if v not in e]
    return cover

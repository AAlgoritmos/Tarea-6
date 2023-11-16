from algorithm_1 import vertex_cover_1
from algorithm_2 import vertex_cover_2
from algorithm_3 import vertex_cover_3
from algorithm_4 import vertex_cover_4
from graph import SimpleGraph
from generate_graph import generate
from time import time

V = [100, 1000, 10000]

E = [300, 2000, 11000]


print("----------------------")
for i in range(len(V)):
    print(f"Test para {V[i]} vértices")
    print(f"Test con {E[i]} aristas")
        
    edges = generate(V[i], E[i])
    G = SimpleGraph(edges)

    t1 = time()
    cover = vertex_cover_1(G)
    t2 = time()
    print(f"Respuesta metodo 1 {cover} de tamaño {len(cover)} tomo tiempo {t2-t1}")
    print()

    t1 = time()
    cover = vertex_cover_2(G)
    t2 = time()
    print(f"Respuesta metodo 2 {cover} de tamaño {len(cover)} tomo tiempo {t2-t1}")
    print()

    t1 = time()
    cover = vertex_cover_3(G)
    t2 = time()
    print(f"Respuesta metodo 3 {cover} de tamaño {len(cover)} tomo tiempo {t2-t1}")
    print()

    t1 = time()
    cover = vertex_cover_4(G)
    t2 = time()
    print(f"Respuesta metodo 4 {cover} de tamaño {len(cover)} tomo tiempo {t2-t1}")

    print()
    print("-------------")
    print()
    print()
    print("-------------------------")

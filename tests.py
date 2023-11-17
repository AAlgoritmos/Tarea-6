from algorithm_1 import vertex_cover_1
from algorithm_2 import vertex_cover_2
from algorithm_3 import vertex_cover_3
from algorithm_4 import vertex_cover_4
from graph import SimpleGraph
from generate_graph import generate
from tqdm import tqdm
from time import time
import pandas as pd
import numpy as np


def test(max_test, v, e):

    a1 = []
    a2 = []
    a3 = []
    a4 = []

    l1 = []
    l2 = []
    l3 = []
    l4 = []

    for i in range(max_test):
        print("Test #", i+1)
        edges = generate(v, e)
        G = SimpleGraph(edges)

        t1 = time()
        cover = vertex_cover_1(G)
        t2 = time()
        a1.append(t2-t1)
        l1.append(len(cover))

        t1 = time()
        cover = vertex_cover_2(G)
        t2 = time()
        a2.append(t2-t1)
        l2.append(len(cover))

        t1 = time()
        cover = vertex_cover_3(G)
        t2 = time()
        a3.append(t2-t1)
        l3.append(len(cover))

        t1 = time()
        cover = vertex_cover_4(G)
        t2 = time()
        a4.append(t2-t1)
        l4.append(len(cover))

    return a1, l1, a2, l2, a3, l3, a4, l4


V = [10000]

E = [[3000]]

max_test = 10

resultados = {"algoritmo1": [],
              "algoritmo2": [],
              "algoritmo3": [],
              "algoritmo4": []}

columns = []

print("----------------------")
for i in range(len(V)):
    print(f"Test para {V[i]} vértices")
    set_e = E[i]
    for e in set_e:

        a1, l1, a2, l2, a3, l3, a4, l4 = test(max_test, V[i], e)

        resultados["algoritmo1"].append(np.mean(a1))
        resultados["algoritmo1"].append(np.std(a1))
        resultados["algoritmo1"].append(np.max(a1))
        resultados["algoritmo1"].append(np.min(a1))
        resultados["algoritmo1"].append(np.mean(l1))
        resultados["algoritmo1"].append(np.std(l1))
        resultados["algoritmo1"].append(np.max(l1))
        resultados["algoritmo1"].append(np.min(l1))

        resultados["algoritmo2"].append(np.mean(a2))
        resultados["algoritmo2"].append(np.std(a2))
        resultados["algoritmo2"].append(np.max(a2))
        resultados["algoritmo2"].append(np.min(a2))
        resultados["algoritmo2"].append(np.mean(l2))
        resultados["algoritmo2"].append(np.std(l2))
        resultados["algoritmo2"].append(np.max(l2))
        resultados["algoritmo2"].append(np.min(l2))

        resultados["algoritmo3"].append(np.mean(a3))
        resultados["algoritmo3"].append(np.std(a3))
        resultados["algoritmo3"].append(np.max(a3))
        resultados["algoritmo3"].append(np.min(a3))
        resultados["algoritmo3"].append(np.mean(l3))
        resultados["algoritmo3"].append(np.std(l3))
        resultados["algoritmo3"].append(np.max(l3))
        resultados["algoritmo3"].append(np.min(l3))

        resultados["algoritmo4"].append(np.mean(a4))
        resultados["algoritmo4"].append(np.std(a4))
        resultados["algoritmo4"].append(np.max(a4))
        resultados["algoritmo4"].append(np.min(a4))
        resultados["algoritmo4"].append(np.mean(l4))
        resultados["algoritmo4"].append(np.std(l4))
        resultados["algoritmo4"].append(np.max(l4))
        resultados["algoritmo4"].append(np.min(l4))

        print(f"Test con {e} aristas")

        columns += ['Media', 'Desviación estándar', 'Maximo', 'Mínimo',
                    'Media', 'Desviación estándar', 'Maximo', 'Mínimo']


data = pd.DataFrame.from_dict(resultados, orient='index', columns=columns)

data.to_excel("Resultados_10000.xlsx")

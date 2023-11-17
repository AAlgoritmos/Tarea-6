from time import time
from graph import SimpleGraph
from generate_graph import generate
from tqdm import tqdm
from algorithm_1 import vertex_cover_1
from algorithm_2 import vertex_cover_2
from algorithm_3 import vertex_cover_3
from algorithm_4 import vertex_cover_4


v = 10000
e = 15000

edges = generate(v, e)
G = SimpleGraph(edges)

t1 = time()
cover = vertex_cover_1(G)
t2 = time()
time2 = t2-t1
print("Time:", time2)
print("Num vertices:", len(cover))

t1 = time()
cover = vertex_cover_2(G)
t2 = time()
time2 = t2-t1
print("Time:", time2)
print("Num vertices:", len(cover))

t1 = time()
cover = vertex_cover_3(G)
t2 = time()
time2 = t2-t1
print("Time:", time2)
print("Num vertices:", len(cover))

t1 = time()
cover = vertex_cover_4(G)
t2 = time()
time2 = t2-t1
print("Time:", time2)
print("Num vertices:", len(cover))

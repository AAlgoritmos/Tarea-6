from sys import stdin
from algorithm_1 import vertex_cover_1
from algorithm_2 import vertex_cover_2
from algorithm_3 import vertex_cover_3
from algorithm_4 import vertex_cover_4
from graph import SimpleGraph
import time


def main():

    edges = []
    algorithm = stdin.readline()
    line = stdin.readline()
    while line:
        u, v = line.split("  ")
        u, v = int(u), int(v)
        edges.append((u, v))
        line = stdin.readline()

    G = SimpleGraph(edges)

    initial_time = time.time()

    if algorithm == "1\n":
        cover = vertex_cover_1(G)
    elif algorithm == "2\n":
        cover = vertex_cover_2(G)
    elif algorithm == "3\n":
        cover = vertex_cover_3(G)
    elif algorithm == "4\n":
        cover = vertex_cover_4(G)
    else:
        raise ValueError("Invalid algorithm number")

    final_time = time.time()

    print("Time: ", final_time - initial_time)
    print("Vertex cover: ", cover)
    print("Size: ", len(cover))


if __name__ == '__main__':
    main()

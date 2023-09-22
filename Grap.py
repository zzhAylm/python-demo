
# Import packages
# %matplotlib inline
import matplotlib.pyplot as plt
from random import uniform, seed
import numpy as np
import time
from igraph import *

if __name__ == '__main__':
    # Create simple network with 0 and 1 as the influential nodes
    source = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5]
    target = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 8, 9]

    g = Graph(directed=True)
    g.add_vertices(range(10))
    g.add_edges(zip(source, target))

    # Plot graph
    g.vs["label"], g.es["color"], g.vs["color"] = range(10), "#B3CDE3", "#FBB4AE"
    plot(g, bbox=(200, 200), margin=20, layout=g.layout("kk"))
    print('PyCharm')
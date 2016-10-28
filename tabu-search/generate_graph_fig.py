#!/usr/bin/env python

import numpy as np
from graphviz import Digraph


def read_graph(fname):
    return np.loadtxt(fname, delimiter=",").astype(np.int64).tolist()


def main():
    adj_matrix = read_graph("graph.txt")
    g = Digraph(format='png')

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if i != j:
                g.edge(str(i), str(j), label=str(adj_matrix[i][j]))

    g.render("figs/tsp_graph.gv")


if __name__ == "__main__":
    main()

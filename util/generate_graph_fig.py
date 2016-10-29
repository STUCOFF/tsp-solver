#!/usr/bin/env python

import re
import argparse
import os
import sys
import numpy as np
from graphviz import Graph


def read_graph(fname):
    return np.loadtxt(fname, delimiter=",").astype(np.int64).tolist()


def main():

    p = argparse.ArgumentParser(
        description='This script is for generate graph figure')
    p.add_argument('-g', '--graph', type=str,
                   help='path to graph csv file', required=True)

    p.add_argument('-o', '--out', type=str,
                   help='output_file', required=True)

    option_args = p.parse_known_args()[0]
    path = option_args.graph
    out_file = option_args.out

    if not os.path.exists(path):
        print("File not found")
        sys.exit(1)

    adj_matrix = read_graph(path)
    g = Graph(format='png')

    for i in range(len(adj_matrix)):
        for j in range(i + 1, len(adj_matrix)):
            g.edge(str(i), str(j), label=str(adj_matrix[i][j]))

    g.render(out_file)


if __name__ == "__main__":
    main()

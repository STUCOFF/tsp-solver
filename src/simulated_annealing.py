#!/usr/bin/env python

import argparse
import os
import sys
import numpy as np
import random

from utils import read_graph, print_graph, get_neighbors, \
    get_cost, find_better_solusion


@profile
def simulated_anealing(graph, step=10000, a=0.5, q=1000, t=50, t_min=0.000001, count_max=100):
    count = 0
    n = len(graph)
    s = np.random.permutation(n).tolist()  # initil solution

    for i in range(step):
        s_next = find_better_solusion(get_neighbors(s), s, graph)

        e = get_cost(s, graph)
        e_next = get_cost(s_next, graph)

        if s == s_next:
            count += 1
        else:
            count = 0

        if e_next < e:
            s = s_next
        else:
            if random.random() <= probability(e, e_next, t):
                s = s_next

        if i % q == 0:  # Equilibrium state
            t = a * t

        if count > count_max:
            return s

    return s


def probability(e1, e2, t):
    return np.exp((e1 - e2) / t)


def main():
    p = argparse.ArgumentParser(
        description='This script is for solve TSP with simulated anealing')
    p.add_argument('-g', '--graph', type=str,
                   help='path to graph csv file', required=True)

    option_args = p.parse_known_args()[0]
    path = option_args.graph

    if not os.path.exists(path):
        print("File not found")
        sys.exit(1)

    graph = read_graph(path)
    s = simulated_anealing(graph)
    print('Answer')
    print("Path:", s, ", Cost:", get_cost(s, graph))


if __name__ == "__main__":
    main()

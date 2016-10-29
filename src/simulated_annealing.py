#!/usr/bin/env python

import numpy as np
import random

from utils import read_graph, print_graph, get_neighbors, \
    get_cost, find_better_solusion


def simulated_anealing(graph, step=1000, a=0.5, q=10, t=50, t_min=0.001):

    n = len(graph)
    s = np.random.permutation(n).tolist()  # initil solution

    for i in range(step):
        s_next = find_better_solusion(get_neighbors(s), s, graph)

        e = get_cost(s, graph)
        e_next = get_cost(s_next, graph)

        if e_next < e:
            s = s_next
        else:
            if random.random() <= probability(e, e_next, t):
                s = s_next

        if i % q == 0:  # Equilibrium state
            t = a * t

        if t < t_min:
            return s

    return s


def probability(e1, e2, t):
    return np.exp((e1 - e2) / t)


def main():
    graph = read_graph("graph.txt")
    s = simulated_anealing(graph)
    print('Answer')
    print("Path:", s, ", Cost:", get_cost(s, graph))


if __name__ == "__main__":
    main()

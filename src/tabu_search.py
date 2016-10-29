#!/usr/bin/env python

import numpy as np
from utils import read_graph, print_graph, swap_list_element, \
    get_neighbors, get_cost, find_better_solusion


def tabu_search(graph, tabu_max=10, step=1000):

    tabu_list = []
    n = len(graph)
    s = np.random.permutation(n).tolist()  # initil solution
    tabu_list.append(s)

    for i in range(step):

        feisible_list = []
        neighbors = get_neighbors(s)

        for x in neighbors:
            if not x in tabu_list:
                feisible_list.append(x)

        s = find_better_solusion(feisible_list, s, graph)

        if not s in tabu_list:
            tabu_list.append(s)

        if len(tabu_list) > tabu_max:
            tabu_list.pop(0)

    return s


def main():
    graph = read_graph("graph.txt")
    s = tabu_search(graph)
    print('Answer')
    print("Path:", s, ", Cost:", get_cost(s, graph))

if __name__ == "__main__":
    main()

#!/usr/bin/env python
import numpy as np


def read_graph(fname):
    return np.loadtxt(fname, delimiter=",").astype(np.int64).tolist()


def print_graph(graph):
    for row in graph:
        print(row)


def swap_list_element(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
    return lst


def get_neighbors(s):
    neighbors = []
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j:
                tmp = s[:]
                neighbors.append(swap_list_element(tmp, i, j))
            else:
                pass

    return neighbors


def get_cost(path, graph):
    cost = 0
    for i in range(len(path) - 1):
        for j in range(1, len(path)):
            cost += graph[i][j]
    return cost


def find_better_solusion(lst, s, graph):
    sums = [get_cost(x, graph) for x in lst]
    i = sums.index(min(sums))

    if sums[i] < sum(s):
        return lst[i]
    else:
        return s


def tab_serch(graph, tab_max=10, n=500):

    for i in range(n):

        n = len(graph)
        s = np.random.permutation(n).tolist()  # initil solution

        tab_list = []

        feisible_list = []
        neighbors = get_neighbors(s)

        for x in neighbors:
            if not x in tab_list:
                feisible_list.append(x)

        s_ = find_better_solusion(feisible_list, s, graph)
        s = s_
        tab_list.append(s_)

        if len(tab_list) > tab_max:
            tab_list.pop(0)

    return s


def main():
    graph = read_graph("graph.txt")
    s = tab_serch(graph)
    print('Answer')
    print(s, ":", get_cost(s, graph))

if __name__ == "__main__":
    main()

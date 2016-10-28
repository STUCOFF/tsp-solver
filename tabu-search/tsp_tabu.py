#!/usr/bin/env python
import numpy as np


def read_graph(fname):
    return np.loadtxt(fname, delimiter=",").astype(np.int64).tolist()


def print_graph(m, graph):
    for row in m:
        print(row, get_cost(row, graph))


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

    return neighbors


def get_cost(path, graph):
    return sum([graph[path[i]][path[i + 1]] for i in range(len(path) - 1)])


def find_better_solusion(lst, s, graph):
    costs = [get_cost(x, graph) for x in lst]
    i = costs.index(min(costs))

    if costs[i] < get_cost(s, graph):
        return lst[i]
    else:
        return s


def tab_serch(graph, tabu_max=10, step=100):

    tabu_list = []
    n = len(graph)
    s = np.random.permutation(n).tolist()  # initil solution

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
    s = tab_serch(graph)
    print('Answer')
    print(s, ":", get_cost(s, graph))

if __name__ == "__main__":
    main()

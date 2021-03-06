#!/usr/bin/env python

import numpy as np
import doctest
doctest.testmod()


def read_graph(fname):
    return np.loadtxt(fname, delimiter=",").astype(np.int64).tolist()


def print_graph(m, graph):
    for row in m:
        print(row, get_cost(row, graph))


def swap_list_element(lst, i, j):
    """Swap list element

    Args:
    lst [int]: one soluton
    i int
    j int

    Returns:
    lst [int]: swaped soluton

    Examples:
    >>> lst = [1,2,3,4]
    >>> swap_list_element(lst, 0, 3)
    [4, 2, 3, 1]
    """

    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
    return lst


def get_neighbors(s):
    """Generate neighbors of one solution s

    Args:
    s [int]: one soluton

    Returns:
    [[int]]: neigbors

    Examples:
    >>> lst = [1,2,3]
    >>> get_neighbors(lst)
    [[2, 1, 3], [3, 2, 1], [1, 3, 2]]
    """

    neighbors = []
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            tmp = s[:]
            neighbors.append(swap_list_element(tmp, i, j))

    return neighbors


def get_cost(path, graph):
    return sum([graph[path[i]][path[i + 1]] for i in range(len(path) - 1)])


def find_better_solusion(feisible_list, s, graph):
    costs = [get_cost(x, graph) for x in feisible_list]
    i = costs.index(min(costs))

    if costs[i] < get_cost(s, graph):
        return feisible_list[i]
    else:
        return s

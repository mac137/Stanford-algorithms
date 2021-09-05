"""
Contraction algorithm and the Minimum Cut Problem by Maciej Trzeciak

"""

from random import choice
from typing import List


f = open('kargerMinCut.txt', 'r')
ls = f.readlines()
f.close()
graph = [list(map(int, i.split('\t')[:-1])) for i in ls]


def get_adjacency_list():
    global graph
    return [i.copy() for i in graph]


def get_index_of_(v: int, adjacency_list: List[List[int]]) -> int:
    index_v = None
    for i, list_v in enumerate(adjacency_list):
        if list_v[0] == v:
            index_v = i
    return index_v


def contraction_alg(adjacency_list: List[List[int]]) -> int:

    while len(adjacency_list) > 2:

        # pick an edge. Here done by picking two nodes at random - so no explicit edges
        list_v1: list = choice(adjacency_list).copy()
        random_v1: int = list_v1[0]
        random_v2: int = choice(list_v1[1:])  # select from all elems of the list but the 0th, cos 0th is v1 itself

        # get indexes of the picked vertices
        index_v1: int = get_index_of_(random_v1, adjacency_list)
        index_v2: int = get_index_of_(random_v2, adjacency_list)

        list_v2: list = adjacency_list[index_v2].copy()

        # merging 2 nodes
        list_v2.extend(list_v1)  # all v1's edges will belong now to v2
        # now v1 will be v2 so rename all v1 into v2
        while random_v1 in list_v2:
            index = list_v2.index(random_v1)
            list_v2.pop(index)

        # remove self loops => the first node in the list should be the only one
        while random_v2 in list_v2:
            list_v2.pop(list_v2.index(random_v2))
        list_v2.insert(0, random_v2)  # add v2 as the first elem of the list

        # since now v1 is v2, rename all v2's in lists of other nodes
        for i, list_v in enumerate(adjacency_list):
            while random_v1 in list_v:
                index = list_v.index(random_v1)
                list_v.pop(index)
                list_v.insert(index, random_v2)

        # insert the proper list related to the situation after merging v1 and v2
        adjacency_list[index_v2] = list_v2
        # remove v1 index from adjacency list
        adjacency_list.pop(index_v1)

    return len(adjacency_list[0])-1


def minimum_cut(trials: int) -> int:
    cut = []

    for i in range(trials):
        cut.append(contraction_alg(get_adjacency_list()))
    return min(cut)


if __name__ == '__main__':

    # my_graph = [[1, 2, 3],
    #             [2, 1, 3, 4],
    #             [3, 1, 2, 4],
    #             [4, 2, 3]]
    # min_cut = minimum_cut(my_graph, 1)
    # print(min_cut)

    trial_number = 100  # for 1000 it will take ~ 1 min
    min_cut = minimum_cut(trial_number)
    print(min_cut)

import numpy as np

def list_is_in(list1, list2):
    '''list_is_in takes in two arrays as input. It then looks through these loops to determine if there are duplicate values if the value is duplicated it replaces the index with true, if not it replaces it with false.'''
    arr = []
    for val in list1:
        try:
            list2.index(val)
            arr.append(True)
        except ValueError:
            arr.append(False)

    return arr



print(list_is_in([1,2,3,4,5], [1,6,7,3,2]))


def mean_normalize(input_array):
    for row in input_array:
        np.mean(row)
        for val in row:



inputArr = [
    [-0.47752694, 2.10771366, 0.59367963],
    [-0.99518782, -0.56534531, 0.01539558],
    [0.44353958, 1.31930398, 2.42232459]
]
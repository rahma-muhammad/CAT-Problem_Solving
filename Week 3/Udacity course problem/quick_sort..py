"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
from cmath import pi


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot= array[0]
        less = [ i for i in array[1:] if i <= pivot]
        greater = [ i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
"""Various Sorting functions Implemented in Python"""
from typing import List


def bubble_sort(array: List[int], reverse: bool = False) -> List[int]:
    """Bubble Sort

    Parameters:
    -----------
    array: List[int]
        Unsorted input array

    Returns:
    --------
    List[int]
        Sorted Array
    """
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if reverse:
                if array[j] < array[j+1]:
                    array[j+1], array[j] = array[j], array[j+1]
            else:
                if array[j] > array[j+1]:
                    array[j+1], array[j] = array[j], array[j+1]
    return array


def insertion_sort(array: List[int], reverse: bool = False) -> List[int]:
    """Insertion Sort

    Parameters:
    -----------
    array: List[int]
        Unsorted input array

    Returns:
    --------
    List[int]
        Sorted array
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        if reverse:
            while j >= 0 and key > array[j]:
                array[j+1] = array[j]
                j -= 1
        else:
            while j >= 0 and key < array[j]:
                array[j+1] = array[j]
                j -= 1
        array[j+1] = key
    return array

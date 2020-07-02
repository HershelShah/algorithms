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


def merge_sort(array: List[int], reverse: bool = False) -> List[int]:
    """Merge Sort

    Parameters:
    -----------
    array: List[int]
        Unsorted input array

    Returns:
    --------
    List[int]
        Sorted Array
    """
    if len(array) > 1:
        left = array[:len(array)//2]
        right = array[len(array)//2:]
        merge_sort(left, reverse=reverse)
        merge_sort(right, reverse=reverse)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if reverse:
                if left[i] >= right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
            else:
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

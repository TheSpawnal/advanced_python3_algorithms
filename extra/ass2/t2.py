#!/usr/bin/env python3
from typing import List

def find_occurrences(array: List[int], n: int) -> int:
    '''
    Find the number of occurrences of `n` in the `array` list

    ### Parameters
    `array`: An  **ordered** array of positive integers

    `n`: int

    ### Return
    The number of occurrences of `n` in `array`
    '''
    if not array:
        return 0
    coord_first = first_occurrence_searcher(array, n)

    if coord_first == -1:
        return 0
    
    coord_last = last_occurrence_searcher(array, n)

    return coord_last - coord_first + 1

def first_occurrence_searcher(array: List[int], n: int) -> int:
    left, right = 0, len(array) -1 
    index_first = -1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == n:
            index_first = mid
            right = mid -1
        elif array[mid] < n:
            left = mid + 1
        else:
            right = mid -1 
        
    return index_first

def last_occurrence_searcher(array: List[int], n: int) -> int:
    left, right = 0, len(array) -1 
    index_last = -1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == n:
            index_last = mid
            left = mid +1
        elif array[mid] < n:
            left = mid + 1
        else:
            right = mid -1 
        
    return index_last


# Alternative / linear search 
# def find_occurrences_simple(array: List[int], n: int) -> int:
#     """counts occurrences linearly.
#     Less efficient O(n) """
#     count = 0
#     for value in array:
#         if value == n:
#             count += 1
#         elif value > n:  # Since array is sorted, we can stop early
#             break
#     return count

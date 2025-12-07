#!/usr/bin/env python3
from typing import List
def smallest_subsequence_length(array: List[int], k: int) -> int:
    '''
    Find the length of the smallest sub-array of `array`
        whose sum of elements is greater than `k`

    ### Parameters
    `array`: An array of positive integers

    `k`: int

    ### Return
    The length of the smallest sub-array
    '''
    array.sort(reverse=True)
    curr_sum=0
    for i, val in enumerate(array):
        curr_sum += val
        if curr_sum > k:
            return i + 1
    return 0

#!/usr/bin/env python3

from typing import List, Union

def is_min_heap(array: List[int]
                ) -> Union[int, bool]:
    '''
    Determine if `array` represents a min heap

    ### Parameters
    `array`: An array of positive integers

    ### Return
    A boolean or int (0|1) for if the `array` is a min heap
    '''
    n=len(array)
    isitHeap = all(
        array[i] <= array[child]
        for i in range(n//2)
        for child in (2*i+1,2*i+2)
        if child <n
    )
    return isitHeap


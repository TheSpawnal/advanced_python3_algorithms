

'''
Findingsriskyneighbourhoods
The water management department has a network of surveillance sensors at 
every corner of the Amsterdam sewage system.
Every sensor reports the level of chemical waste in the water.
Each day the sensors are queried for an updated measurement roughly 
by neighbourhood. Therefore, the measurements from sensors that are 
in close proximity to each other are initially stored on consecutive 
array locations.
The water management department takes in water from a few different 
random neighborhoods at a time for treatment, 
but has to make sure the level of chemical waste remains below 
a certain level. If the level is too high, nature and people will suffer.
You are tasked with implementing an algorithm that finds the smallest subsequence 
in the readings (positive integers) whose sum of elements exceed 
the threshold definedbythewatermanagement department. 

If no such subsequence exists your algorithm should return 0.
Example1. Thesmallest_subsequence_length function takes two parameters:
• array(list[int]): Anarrayofpositive integers
• k(int)
The function returns a the length of the smallest subsequence as an Integer.
Call: smallest_subsequence_length([1, 2, 3, 4, 5, 6, 7, 8], 20)
Returns (int): 3

'''




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

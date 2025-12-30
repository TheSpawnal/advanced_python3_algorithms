
'''
The cooperation between the water management and health authorities has 
been very successful and thanks to your programming skills, 
the new covid measurement system is about to go online for every
city in the Netherlands. However, after a long discussion with your colleague, 
you both realized that some of the new algorithms will not scale to 
the new amounts of readings you will have to handle. 
In particular, the newalgorithmsincludeanenormousamountofcallstoafunctioncalled 
findmin. You decided to implement a newdatastructure, and your colleague did a first attempt last week. 
Since this is a hugeopportunity, you both want to makesure thedatastructure was 
implemented correctly. You task is to implement an algorithm that checks it a 
given integer array represents a min-heap or not.

Example3. The is_min_heap function takes one parameters:
• array(list[int]): Anarrayofpositive integers
The function returns a Boolean or an Integer
Call: is_min_heap([1, 2, 5, 3, 4, 6, 7])
Returns (Union[int, bool]): 1|True
'''
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


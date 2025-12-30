
'''
this code aims to implement a binary search algorithm in a recursive way. We can assume arr array is sorted.

Define binarysearch(arr, x)
    If the array is empty
        Return-1

    Set mid var to half of the array length

    If the middle value of the array is the searched value, then return the middle index
    Else if the middle value is smaller than the searched value
        then set the result to binarysearch(subarray starting from mid+1 onward, x)
        Return the result+index of the middle index+1, if result is -1 return-1

    else return the result of binarysearch(subarray from index 0 to mid-1, x)
'''

def binary_search(arr, x):
    if not arr:
        return -1
    mid = len(arr) // 2

    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        result = binary_search(arr[mid+1:],x)
        return result + mid + 1 if result != -1 else -1
    else:
        return binary_search(arr[:mid],x)
    
'''
which are true

-the algo is sub-optimal, since on line 30, the array passed to binary_Search also includes
    arr[mid] which we've already proven not equal x.FALSE
 The slicing notation in Python allows to quickly generate a sublist. arr[:mid] means that
 the array sublist has to range from the first index up to mid, excluding the last index (mid).
 The slice notation includes the starting index but excludes the last. Therefore we are not
 considering arr[mid] by returning the sublist arr[:mid].

-The code is correct but using a linked list would reduce the execution time.FALSE
Using a linked list would not reduce the execution time. Getting the mid element would
 take O(n) for a list while it would take only O(1) to an array. Also, creating a new sub array
 requires O(k) where k is the number of elements to copy, while we would need to traverse
 the whole list (O(n)) in order to create a sublist from the second half of the list.

-The code is correct and wouldn't be faster with a linked list. TRUE

-Line 28 is not correct Python syntax.False 
 Line 28 is correct and contains a ternary operator. Ternary operators allow to quickly write
 simple if-else statements in a single line. They follow the syntax: A if CONDITION else B,
 and it returns A if CONDITION is true, otherwise it returns B. It’s often used in return
 statements and variable assignment

- Being a Recursive algorithm, if no correct value is found, the algorithm would keep running in a loop.FALSE
Correct recursive algorithms contain a termination condition which in this case is the first
 if on lines 20 and 21. If the item hasn’t been found then it will return-1. In the worst case
 the algorithm will terminate in O(log(n)).
'''



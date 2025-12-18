

 BINARY SEARCH MODIFICATION
• Modify binary search to count elements < x
• Must be iterative (10 pts), recursive only gets partial
• Part B: Loop invariant proof (8 pts)


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

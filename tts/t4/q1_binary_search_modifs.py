

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


#  BINARY SEARCH MODIFICATION
# • Modify binary search to count elements < x
# • Must be iterative , recursive with a second strategy
# • Part B: Loop invariant proof for both version delivered. 


def count_less_than_iterative(arr, x):
    """
    Iterative binary search to count elements < x.
    Strategy: Find leftmost position where arr[i] >= x
    """
    if not arr:
        return 0
    
    left, right = 0, len(arr) - 1
    result = len(arr)  # If all elements < x
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] < x:
            left = mid + 1
        else:
            result = mid
            right = mid - 1
    
    return result


def count_less_than_recursive_v1(arr, x, offset=0):
    """
    Recursive binary search - Strategy 1: Track offset through recursion
    """
    if not arr:
        return offset
    
    mid = len(arr) // 2
    
    if arr[mid] < x:
        return count_less_than_recursive_v1(arr[mid+1:], x, offset + mid + 1)
    else:
        return count_less_than_recursive_v1(arr[:mid], x, offset)


def count_less_than_recursive_v2(arr, x, left=0, right=None):
    """
    Recursive binary search - Strategy 2: Pass indices instead of slicing
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return left
    
    mid = (left + right) // 2
    
    if arr[mid] < x:
        return count_less_than_recursive_v2(arr, x, mid + 1, right)
    else:
        return count_less_than_recursive_v2(arr, x, left, mid - 1)


# Test cases
if __name__ == "__main__":
    test_arrays = [
        ([1, 2, 3, 4, 5, 6, 7], 4),
        ([1, 3, 5, 7, 9], 6),
        ([2, 2, 2, 2], 2),
        ([1, 2, 3], 10),
        ([], 5),
        ([5], 3),
        ([5], 7)
    ]
    
    for arr, x in test_arrays:
        i = count_less_than_iterative(arr, x)
        r1 = count_less_than_recursive_v1(arr, x)
        r2 = count_less_than_recursive_v2(arr, x)
        print(f"arr={arr}, x={x}")
        print(f"  Iterative: {i}, Recursive_v1: {r1}, Recursive_v2: {r2}")
        print(f"  Verification: {sum(1 for elem in arr if elem < x)}")
        print()


'''
loop invariant iterative version.
Loop invariant: 
At the start of each iteration: all elements in arr[0: result] are >=x, 
and all elements in arr[result:] are unchecked OR < x
Initialization:
-result = len(arr) (assumes all elements might be < x)
-Invariant holds : no elements in arr[0:len(arr)] confirmed >= x yet
Maintenance:
If arr[mid] < x: all elements in arr[left:mid+1] are < x, move left = mid + 1
If arr[mid] >= x: element at mid is >= x, update result = mid, search left half
Invariant preserved: result always points to leftmost known >= x position
Termination:
Loop exits when left > right
result holds the leftmost index where arr[i] >= x
Count of elements < x = result



FUNCTION count_less_than_iterative(arr, x)
    IF arr is empty THEN
        RETURN 0
    END IF
    
    SET left = 0
    SET right = length(arr) - 1
    SET result = length(arr)
    
    WHILE left <= right DO
        SET mid = floor((left + right) / 2)
        
        IF arr[mid] < x THEN
            SET left = mid + 1
        ELSE
            SET result = mid
            SET right = mid - 1
        END IF
    END WHILE
    
    RETURN result
END FUNCTION
'''




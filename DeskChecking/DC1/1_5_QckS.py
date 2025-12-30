'''
QuickSort without In-Place Sorting: 
The code implements a variant of QuickSort that doesn't perform in-place sorting. 
In-place sorting would involve swapping elements within the original list to sort them, 
while this implementation creates new lists for smaller and greater elements.
Trade-offs: The non-in-place approach might be easier to understand and implement, 
but it's less memory-efficient as it creates additional lists. 
In-place sorting, while potentially more complex to implement, is more memory-efficient.


 Pseudocode
 Define swap(arr, i, j)
      Swap values of arr at index i and j

 Define quicksort(ar)
      If there is one or less elements return ar

    Pick the middle element as pivot
    Create two empty lists, one for objects smaller and one for objects greater than the pivot
    If you are analyzing the pivot then skip to the next object in list
    Put elements greater or same as the pivot in the list for the greater objects
    Put elements smaller than the pivot in the list fot the smaller objects

    Set as the left list the quicksorted list with objects smaller than the pivot
    Set as the right list the quicksorted list with objects greater than the pivot
    Return the left list, appending the pivot, appending the right list
'''


class Order:
    def init (self, id, selectiontime, shippingtime):
        self.id: int = id
        self.selectiontime: int = selectiontime
        self.shippingtime: int = shippingtime
 
    def eq (self, other):
        return (self.selectiontime + self.shippingtime) == (other.selectiontime + other.shippingtime)
 
    def gt (self, other):
        return (self.selectiontime + self.shippingtime)>(other.selectiontime + other.shippingtime)



def swap(arr: List[Order], i: int, j: int):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def quicksort(ar: List[Order]):
    if len(ar)<= 1:
        return ar

    mid = len(ar)//2 #line11
    pivot = ar[mid]

    smaller,greater = [],[] 
 
    for i, val in enumerate(ar):
        if i == mid:
            continue
        if val<pivot:
            smaller.append(val)
        elif val>pivot:
            greater.append(val)
    left = quicksort(smaller)
    right = quicksort(greater)
    return left+[pivot]+right
  
'''
which of the following statements about the code are true:

1/The implementation is correct and contains no bug.FALSE

2/The case of val == pivot is not specified, for this reason all the values equal to the pivot will be lost at every iteration.TRUE
The behaviour when val == pivot is not specified in the if. This poses no problem for the
pivot itself since it is added in the return statement at the end of the function. 
The problem concerns other objects that have the same value as the pivot but a different position in the
index. No condition is defined in this case therefore all objects equal to the pivot (but not
 the pivot) will be lost at every iteration. ( nasty)

3/The pivot is not included in the left sub-list nor the right sub-list, therefore its value will be lost during the execution. FAlSE

4/The variable mid defined at line 11 may be a decimal number when len(arr) is an odd number. Thus causing the code to fail, since we cannot use a decimal value as an array index. FALSE
The code mid = len(ar)//2 will never return a decimal number since the // operand is a division with flooring operand. This means that after dividing the number the operand
rounds the result by flooring it (removing the decimal part and keeping the integer only).

 '''


'''
Referring back to the searching problem (see 2_1_4), observe that
if the subarray being searched is already sorted, the searching algorithm can
check the midpoint of the subarray against v and eliminate half of the
subarray from further consideration. The binary search algorithm repeats
this procedure, halving the size of the remaining portion of the subarray
each time. Write pseudocode, either iterative or recursive, for binary search.
Argue that the worst-case running time of binary search is Θ(lg n).
'''

# Procedure B-S takes sorted array, A, a value x, and a range [low:high] of the
# array, in which we search of the value x. The procedure compares x to the array
# entry at the midpoint of the range and decides to eliminate half the range
# from further consideration. We give both iterative and recursive versions, u lucky mf,
# each of which returns either an index i such that A[i] = x, or NIL if no entry of A[low:high]
# contains the value x. The initial call to either version should have the parameters A,x,1,n.

'''
ITERATIVE-Binary-Search(A,x, low, high)
  while low <= high
    mid = [(low+high)//2]
    if x == A[mid]
      return mid
    elseif x > A[mid]
      low = mid + 1
    else high = mid - 1
  return NIL
'''

'''
Recursive-Binary-Search(A,x,low, high)
  if low > high
    return NIL
  mid = [(low+high)//2]
  if x == A[mid]
    return mid
  elseif x > A[mid]
    return Recursive-Binary-Search(A,x,mid + 1, high)
  else return Recursive-Binary-Search(A,x,low, mid-1)
'''

Both procedures terminate the search unsuccessfully when the range is empty
(e,g, low > high) and terminate successfully if the value x has been found. 
Based on the comparison of x to the middle element in the searched range, the search continues
with range halved. The recurrence for thhese procedures is therefore T(n) = T(n/2)+ Theta(1),
whose solution is T(n) = Theta(lg n).






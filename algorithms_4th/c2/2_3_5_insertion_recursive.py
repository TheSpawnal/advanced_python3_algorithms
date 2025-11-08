#  You can also think of insertion sort as a recursive algorithm. In order to sort
#  A[1 : n], recursively sort the subarray A[1 : n – 1] and then insert A[n] into
#  the sorted subarray A[1 : n – 1]. Write pseudocode for this recursive version
#  of insertion sort. Give a recurrence for its worst-case running time.

# The following recursive algorithm gives the desired result when called with
# a = 1 and b = n.

BinSearch(a,b,v)
if then a > b
    return NIL
end if
m = [(a+b)//2]
if then m = v
    return m
end if
if then m < v
    return BinSearch(a,m,v)
end if
return BinSearch(m+1,b,v)

Note that the initial call should be BinSearch(1, n, v). Each call results in
a constant number of operations plus a call to a problem instance where the
quantity "b-a" falls by at least a factor of two. So, the runtime satisfies the
recurrence T(n) = T(n/2) + c. So, T(n) ∈ Θ(lg(n))

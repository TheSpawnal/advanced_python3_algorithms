

RANDOMIZED-PARTITION(A, p, r)
 1 i = RANDOM(p, r)
 2 exchange A[r] with A[i]
 3 return PARTITION(A, p, r)

RANDOMIZED-QUICKSORT(A, p, r)
 1 if p < r
 2  q = RANDOMIZED-PARTITION(A, p, r)
 3 RANDOMIZED-QUICKSORT(A, p, q – 1)
 4 RANDOMIZED-QUICKSORT(A, q + 1, r)


# Why do we analyze the expected running time of a randomized algorithm 
# and not its worst-case running time?

We analyze the expected run time because it represents the more typical time cost. 
Also, we are doing the expected run time over the possible randomness used 
during computation because it can't be produced adversarially, 
unlike when doing expected run time over all possible inputs to the algorithm.


# When RANDOMIZED-QUICKSORT runs, how many calls are made to the random number generator 
# RANDOM in the worst case? How about in the best case? Give your answer in terms of 
# Θ-notation.

In the worst case, the number of calls to 
RANDOM is T(n)=T(n−1)+1=n=Θ(n).
As for the best case,
T(n)=2T(n/2)+1=Θ(n).
This is not too surprising, because each third element (at least) gets picked as pivot.
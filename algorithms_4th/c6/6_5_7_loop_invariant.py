MAX-HEAP-INCREASE-KEY(A, x, k)
 1 if k < x.key
 2 error “new key is smaller than current key”
 3 x.key = k
 4 find the index i in array A where object x occurs
 5while i > 1 and A[PARENT(i)].key < A[i].key
 6 exchange A[i] with A[PARENT(i)], updating the information that maps priority queue objects to array indices
 7 i = PARENT(i)



# Argue the correctness of MAX-HEAP-INCREASE-KEY using the following
#  loop invariant:
#  At the start of each iteration of the while loop of lines 5–7:
#  a. If both nodes PARENT(i) and LEFT(i) exist, then A[PARENT(i)].key ≥
#  A[LEFT(i)].key.
#  b. If both nodes PARENT(i) and RIGHT(i) exist, then A[PARENT(i)].key ≥
#  A[RIGHT(i)].key.
#  c. The subarray A[1 : A.heap-size] satisfies the max-heap property,
#  except that there may be one violation, which is that A[i].key may be
#  greater than A[PARENT(i)].key.
#  You may assume that the subarray A[1 : A.heap-size] satisfies the max-heap
#  property at the time MAX-HEAP-INCREASE-KEY is called.

Correctness Proof of MAX-HEAP-INCREASE-KEY Using Loop Invariant
Loop Invariant
At the start of each iteration of the while loop of lines 5–7:
a. If both nodes PARENT(i) and LEFT(i) exist, then A[PARENT(i)].key ≥ A[LEFT(i)].key.
b. If both nodes PARENT(i) and RIGHT(i) exist, then A[PARENT(i)].key ≥ A[RIGHT(i)].key.
c. The subarray A[1 : A.heap-size] satisfies the max-heap property, except that there may be one violation: A[i].key may be greater than A[PARENT(i)].key.

Proof Structure
We must prove three things:

Initialization: The invariant holds before the first iteration
Maintenance: If the invariant holds before an iteration, it holds after the iteration
Termination: When the loop terminates, the invariant gives us a useful property


1. Initialization (Before the first iteration)
Before line 5: We have just executed line 3 (x.key = k) and line 4 (found index i).
Given: The subarray A[1 : A.heap-size] satisfied the max-heap property before the call.
After line 3: We increased x.key (at position i). This may violate the max-heap property only between node i and PARENT(i), since we only modified one node.
Proving part (a):

If both PARENT(i) and LEFT(i) exist, then LEFT(i) is a child of PARENT(i)
Since we only modified position i, and LEFT(i) ≠ i (they're at different levels), the relationship between PARENT(i) and LEFT(i) was not affected
The max-heap property held before, so A[PARENT(i)].key ≥ A[LEFT(i)].key still holds

Proving part (b):

By the same reasoning, if both PARENT(i) and RIGHT(i) exist, they were in a valid max-heap relationship before
We didn't modify either of these nodes (we only modified i)
Therefore A[PARENT(i)].key ≥ A[RIGHT(i)].key still holds

Proving part (c):

The only node we modified is at position i
This node's key increased, so:

It still satisfies the max-heap property with respect to its children (if increasing the parent's value, it remains ≥ children)
It may violate the property with respect to PARENT(i) (we might now have A[i].key > A[PARENT(i)].key)


All other nodes are unchanged, so their max-heap relationships are preserved
Therefore, the only possible violation is A[i].key > A[PARENT(i)].key

Conclusion: The invariant holds before the first iteration. ✓

2. Maintenance (Loop iteration preserves the invariant)
Assume: The invariant holds at the start of an iteration where the loop condition is true (i > 1 and A[PARENT(i)].key < A[i].key).
During the iteration (lines 6-7):

Line 6: Exchange A[i] with A[PARENT(i)]
Line 7: Set i = PARENT(i)

Let's denote:

i_old = the value of i before the iteration
i_new = PARENT(i_old) = the value of i after line 7

After the exchange:

The node that was at position i_old is now at position PARENT(i_old) = i_new
The node that was at position PARENT(i_old) is now at position i_old

Proving part (a) for the next iteration:
We need to show: If both PARENT(i_new) and LEFT(i_new) exist, then A[PARENT(i_new)].key ≥ A[LEFT(i_new)].key.
Case 1: LEFT(i_new) = i_old (the left child of i_new is where we just swapped from)

Before the swap, by invariant part (c), we had A[i_old].key > A[PARENT(i_old)].key (that's why we entered the loop)
After the swap, A[i_new] now contains the larger key
We need A[PARENT(i_new)].key ≥ A[i_old].key (after swap)
The node at i_old (after swap) came from PARENT(i_old), which by invariant part (a) satisfied A[PARENT(PARENT(i_old))].key ≥ A[LEFT(PARENT(i_old))].key
This may not hold immediately, which is why we have invariant part (c) allowing this one violation

Case 2: LEFT(i_new) ≠ i_old

LEFT(i_new) is in a different subtree
Neither LEFT(i_new) nor PARENT(i_new) was involved in the swap (except PARENT(i_new) might be affected if it equals some specific position)
By invariant parts (a) and (b) from before, and since these nodes weren't swapped, the relationship is preserved

Proving part (b) for the next iteration:

By symmetric reasoning to part (a), considering RIGHT(i_new) instead of LEFT(i_new)

Proving part (c) for the next iteration:
We need to show the max-heap property holds everywhere except possibly A[i_new].key > A[PARENT(i_new)].key.

At position i_old (after swap): This position now holds the smaller key (from PARENT(i_old)). Since this key was ≥ both children of PARENT(i_old) before (by invariant parts a and b), and i_old has smaller children than PARENT(i_old) had (being lower in the tree), the max-heap property holds here.
At position i_new (after swap): This position now holds the larger key (from i_old). It satisfies the max-heap property with respect to its children because:

The node at i_old satisfied heap property with its children before
We moved this larger key up, making it even more suitable for the parent position


The only possible violation: A[i_new].key might be > A[PARENT(i_new)].key, which is exactly what invariant part (c) allows.

Conclusion: The invariant is maintained after each iteration. ✓

3. Termination
The loop terminates when: i = 1 OR A[PARENT(i)].key ≥ A[i].key
Case 1: i = 1

The node is now at the root
There is no parent, so no violation can exist with the parent
By invariant part (c), there are no other violations
The max-heap property holds completely ✓

Case 2: A[PARENT(i)].key ≥ A[i].key

The one allowed violation (part c) no longer exists
By invariant parts (a), (b), and (c), the entire array satisfies the max-heap property ✓


Conclusion
By the loop invariant:

Initialization: The invariant holds before the loop starts
Maintenance: Each iteration preserves the invariant while moving the violation up the tree
Termination: When the loop ends, the invariant guarantees that the max-heap property is fully restored

Therefore, MAX-HEAP-INCREASE-KEY is correct. It restores the max-heap property by bubbling the increased key up the tree until it finds its proper position, maintaining all other heap relationships throughout the process.

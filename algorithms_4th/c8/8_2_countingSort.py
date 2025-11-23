

COUNTING-SORT(A, n, k)
  1 let B[1 : n] and C [0 : k] be new arrays
  2 for i = 0 to k
  3     C [i] = 0
  4 for j = 1 to n
  5     C [A[j]] = C [A[j]] + 1
  6// C [i] now contains the number of elements equal to i.
  7 for i = 1 to k
  8     C [i] = C [i] + C [i – 1]
  9// C [i] now contains the number of elements less than or equal to i.
 10// Copy A to B, starting from the end of A.
 11 for j = n downto 1
 12     B[C [A[j]]] = A[j]
 13     C [A[j]] = C [A[j]] – 1 // to handle duplicate values
 14 return B


3/Suppose that we were to rewrite the for loop header in line 11 of the
 COUNTING-SORT as
 11for j = 1 to n
 Show that the algorithm still works properly, but that it is not stable. Then
 rewrite the pseudocode for counting sort so that elements with the same
 value are written into the output array in order of increasing index and the
 algorithm is stable.

 4/Prove the following loop invariant for COUNTING-SORT:
 At the start of each iteration of the for loop of lines 11–13, the last
 element in A with value i that has not yet been copied into B
 belongs in B[C [i]].


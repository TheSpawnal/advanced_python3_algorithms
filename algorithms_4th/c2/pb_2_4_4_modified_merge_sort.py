# algorithm M.Merge-Sort for Modified Merge Sort. In addition
# to sorting A, it will also keep track of the number of inversions. The algorithm
# works as follows. When we call M.Merge-Sort(A,p,q) it sorts A[p..q] and
# returns the number of inversions in the elements of A[p..q], so lef t and right
# track the number of inversions of the form (i, j) where i and j are both in
# the same half of A. When M.Merge(A,p,q,r) is called, it returns the number
# of inversions of the form (i, j) where i is in the first half of the array and j
# is in the second half. Summing these up gives the total number of inversions
# in A. The runtime is the same as that of Merge-Sort because we only add an
# additional constant-time operation to some of the iterations of some of the
# loops. Since Merge is Θ(n log n), so is this algorithm.


Algorithm 6 M.Merge-Sort(A, p, r)
if p < r then
    q = [(p + r)//2]
    lef t = M.Merge − Sort(A, p, q)
    right = M.Merge − Sort(A, q + 1, r)
    inv = M.Merge(A, p, q, r) + lef t + right
    return inv
end if
return 0

Algorithm 7 M.Merge(A,p,q,r)
inv = 0
n1 = q − p + 1
n2 = r − q
let L[1, ..n1] and R[1..n2] be new arrays
for i = 1 to n1 do
    L[i] = A[p + i − 1]
end for
for j = 1 to n2 do
    R[j] = A[q + j]
end for
i = 1
j = 1
k = p
while i 6= n1 + 1 and j 6= n2 + 1 do
    if L[i] ≤ R[j] then
        A[k] = L[i]
        i = i + 1
    else A[k] = R[j]
        inv = inv + j // This keeps track of the number of inversions between
the left and right arrays.
        j = j + 1
    end if
    k = k + 1
end while
if i == n1 + 1 then
    for m = j to n2 do
        A[k] = R[m]
        k = k + 1
    end for
end if
if j == n2 + 1 then
    for m = i to n1 do
        A[k] = L[m]
        inv = inv + n2 // Tracks inversions once we have exhausted the right
//array. At this point, every element of the right array contributes an inversion.
        k = k + 1
    end for
end if
return inv

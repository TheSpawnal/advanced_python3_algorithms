
'''
You need to store a set of n keys in a hash table of size m. 
Show that if the keys are drawn from a universe U with  
|U| > (n−1)m
then U has a subset of size n consisting of keys that all 
hash to the same slot. So that the worst-case searching 
time for hashing with chaining is Θ(n). 




Pigeonhole Principle Applied to Hash Table Collisions
Proof
Given:

Hash table with m slots
n keys to store
Universe U where |U| > (n-1)m

To prove: There exists a subset of n keys from U that all hash to the same slot.

Proof by Pigeonhole Principle
Step 1: Partition the universe U
For each slot i ∈ {0, 1, ..., m-1}, define:

S_i = {k ∈ U : h(k) = i}

The sets S_0, S_1, ..., S_{m-1} partition U (every key hashes to exactly one slot).
Step 2: Apply contradiction
Assume for contradiction that no slot contains n or more keys from U. Then:

|S_i| ≤ n-1 for all i ∈ {0, 1, ..., m-1}

Step 3: Count total keys
If each of the m slots contains at most n-1 keys:
|U| = Σ(i=0 to m-1) |S_i| ≤ m(n-1) = (n-1)m
Step 4: Contradiction
But we're given that |U| > (n-1)m.
This contradicts our assumption, so there must exist at least one slot j where |S_j| ≥ n.
Step 5: Conclusion
Since |S_j| ≥ n, we can select any n keys from S_j. These n keys all hash to slot j, forming the required subset.

Worst-Case Search Time Implication
Consequence: When all n keys hash to the same slot:

That slot's chain contains all n elements
Other m-1 slots remain empty
Searching for a key in the worst case requires traversing the entire chain
CHAINED-HASH-SEARCH runs LIST-SEARCH on a list of length n
Therefore: Θ(n) worst-case search time


Key Insight
The pigeonhole principle guarantees that for any hash function h and sufficiently large universe 
|U| > (n-1)m, there will always exist a "bad" set of n keys that defeat the hash function 
by all colliding in the same slot. This is why no single hash function can guarantee 
good average-case performance for all possible key sets - adversarial inputs always exist.

'''




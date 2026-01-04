

# • Given hash function k mod 10
# • Part A: Identify collisions
# • Part B: Suggest improved function + reasoning
#  requirements CRITERIA
# • Collisions: slots 2 & 5 worst offenders
# • Improved hash must reduce collisions

#Hash function: h(k) = k mod 10
#Keys to insert: {12, 22, 32, 42, 52, 5, 15, 25, 35, 45}

'''
FUNCTION analyze_collisions(keys, hash_function):
  slots <- empty dictionary(slot-> list of keys)

  FOR each key in keys:
    slot<- hash_fnction(key)
    append key to slots[slot]

  collisions <- empty list
  FOR each slots, key_lists in slots:
    if length(key_list) > 1:
      append(slot, key_list) to collisions

  RETURN slots, collisions
'''


# Slot 2: [12, 22, 32, 42, 52]  →  5 keys, 4 collisions
# Slot 5: [5, 15, 25, 35, 45]   →  5 keys, 4 collisions
# ─────────────────────────────────────────────────────
# Total collisions: 8
# Slots used: 2 out of 10 (20% utilization)


'''
Part B improved hash function

FUNCTION improved_hash(key, table_size):
    A ← 31              # Use prime multiplier to break digit patterns
    # Multiplicative scatter then reduce
    hash_value ← (key * A) mod table_size
    RETURN hash_value


FUNCTION alternative_hash(key, table_size):
    # For table_size = 10, use prime near it
    prime ← 7  # largest prime < 10
    hash_value ← key mod prime
    RETURN hash_value 
'''

"""
#Hash function: h(k) = k mod 10
#Keys to insert: {12, 22, 32, 42, 52, 5, 15, 25, 35, 45}
Label the slots of our table be 0,1,2,...,8.
Numbers which appear to the left in the table have been inserted later.

0:nil
1:nil
2:12,22,32,42,52
3:nil
4:nil
5: 5, 15, 25, 35, 45
6:nil
7: nil
8:nil
9:nil

5 keys in 2 -> 4 collsions
5 keys in 5 -> 4 collisions.
"""


# **Output:**
# k mod 10: 8 collisions
#   slot 2: [12, 22, 32, 42, 52]
#   slot 5: [5, 15, 25, 35, 45]
# k mod 7: 5 collisions
#   slot 0: [42, 35]
#   slot 1: [22, 15]
#   slot 3: [52, 45]
#   slot 4: [32, 25]
#   slot 5: [12, 5]
# (31*k) mod 11: 1 collisions
#   slot 9: [12, 45]
'''
Issue: mod 10 captures only last digit.
Solution: use prime modulus.
-> Primes have no common factors with key patterns.

Isue: Arithmetic sequences collide.
Solution:mutilplicative constant -> scrambles linear relationship.

Issue: Poor slot utilization;
Solution: larger prime table-> more bukckets  + prime  = better distribution.






ex : 
Professor Marley hypothesizes that he can obtain substantial performance gains
by modifying the chaining scheme to keep each list in sorted order. 
How does the professor's modification affect the running time for 
successful searches, unsuccessful searches, insertions, and deletions?

Successful searches: no difference, Θ(1+log(α)).
Unsuccessful searches: faster but still Θ(1+log(α)).
Insertions: same as successful searches Θ(1+α).
Deletions: same as before if we use doubly linked lists, Θ(1).

Professor Marley's hypothesis is wrong. No substantial gains:
Unsuccessful search: ~2x faster (nice, but not asymptotic improvement)
Insertion: significantly worse
Others: unchanged
The overhead of maintaining sorted order outweighs the minor search improvement.
'''

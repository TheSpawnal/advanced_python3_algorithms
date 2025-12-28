

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
    # Use prime multiplier to break digit patterns
    A ← 31  # or 37, 61 — small primes work well
    
    # Multiplicative scatter then reduce
    hash_value ← (key * A) mod table_size
    
    RETURN hash_value


FUNCTION alternative_hash(key, table_size):
    # For table_size = 10, use prime near it
    prime ← 7  # largest prime < 10
    
    hash_value ← key mod prime
    
    RETURN hash_value 
'''

def analyze_hash(keys, hash_fn, table_size):
    slots = {}
    for k in keys:
        s = hash_fn(k, table_size)
        slots.setdefault(s, []).append(k)
    
    collisions = sum(len(v) - 1 for v in slots.values() if len(v) > 1)
    return slots, collisions


def h_original(k, _):
    return k % 10

def h_prime_mod(k, _):
    return k % 7

def h_multiplicative_prime(k, _):
    return (31 * k) % 11


keys = [12, 22, 32, 42, 52, 5, 15, 25, 35, 45]

for name, fn, sz in [
    ("k mod 10", h_original, 10),
    ("k mod 7", h_prime_mod, 7),
    ("(31*k) mod 11", h_multiplicative_prime, 11)
]:
    slots, col = analyze_hash(keys, fn, sz)
    print(f"{name}: {col} collisions")
    for s in sorted(slots):
        if len(slots[s]) > 1:
            print(f"  slot {s}: {slots[s]}")


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
Solution: use prime modulus.-> Primes have no common factors with key patterns.

Isue: Arithmetic sequences collide.
Solution:mutilplicative constant -> scrambles linear relationship.

Issue: Poor slot utilization;
Solution: larger prime table-> more bukckets  + prime  = better distribution.
'''

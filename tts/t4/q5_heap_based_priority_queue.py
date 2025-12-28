
'''
Write HEAP-INCREASE-KEY and MAX-HEAP-INSERT
•Must maintain max-heap property

• HEAP-INCREASE-KEY: must bubble up correctly
• MAX-HEAP-INSERT: must use increase-key
• Points lost for logical errors (not checking parent, wrong 
dummy value)


FUNCTION MAX-HEAP-INSERT(A, heap_size, key):
    ──────────────────────────────────────────────
    # Step 1: Expand heap with dummy value
    #         Use -∞ to guarantee increase is valid
    ──────────────────────────────────────────────
    
    heap_size ← heap_size + 1
    A[heap_size - 1] ← -∞      # dummy: smallest possible
    
    ──────────────────────────────────────────────
    # Step 2: Use INCREASE-KEY to place correctly
    #         This handles all bubble-up logic
    ──────────────────────────────────────────────
    
    HEAP-INCREASE-KEY(A, heap_size - 1, key)
    
    RETURN heap_size


Why -∞ as dummy?
─────────────────
1. Any real key ≥ -∞, so increase-key precondition holds
2. Guarantees the new node will bubble up correctly
3. Using 0 or None would fail for negative keys

'''

import math

class MaxHeap:
    def __init__(self):
        self.data = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def heap_increase_key(self, i, new_key):
        if new_key < self.data[i]:
            raise ValueError("new key smaller than current")
        
        self.data[i] = new_key
        
        while i > 0 and self.data[self.parent(i)] < self.data[i]:
            p = self.parent(i)
            self.data[i], self.data[p] = self.data[p], self.data[i]
            i = p
    
    def insert(self, key):
        self.data.append(-math.inf)
        self.heap_increase_key(len(self.data) - 1, key)
    
    def __str__(self):
        return str(self.data)


h = MaxHeap()
for k in [20, 12, 18, 8, 5]:
    h.insert(k)
print(f"after build: {h}")

h.insert(17)
print(f"after insert 17: {h}")

h.heap_increase_key(4, 25)
print(f"after increase index 4 to 25: {h}")
```

**Output:**
```
after build: [20, 12, 18, 8, 5]
after insert 17: [20, 12, 18, 8, 5, 17]
after increase index 4 to 25: [25, 20, 18, 8, 12, 17]





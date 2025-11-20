#  Professor Uriah suggests replacing the while loop of lines 5–7 in MAX
# HEAP-INCREASE-KEY by a call to MAX-HEAPIFY. Explain the flaw in the
#  professor’s idea.

The Professor's (Flawed) Idea:
Replace the while loop in MAX-HEAP-INCREASE-KEY with a call to MAX-HEAPIFY.

Current Correct Implementation:
MAX-HEAP-INCREASE-KEY(A, i, key)
    if key < A[i]
        error "new key is smaller than current key"
    A[i] = key
    while i > 1 and A[PARENT(i)] < A[i]          # Lines 5-7
        exchange A[i] with A[PARENT(i)]
        i = PARENT(i)

Professor's Incorrect Suggestion:
pythonMAX-HEAP-INCREASE-KEY(A, i, key)  // WRONG!
    if key < A[i]
        error "new key is smaller than current key"
    A[i] = key
    MAX-HEAPIFY(A, i)  // This is the problem!

Why This Doesn't Work
1. Direction of Violation
MAX-HEAPIFY assumes the violation is DOWNWARD (parent smaller than children)
MAX-HEAP-INCREASE-KEY creates a violation UPWARD (child larger than parent)

When you increase a key, the node might become larger than its parent, 
but it's still likely larger than or equal to its children. 
MAX-HEAPIFY moves elements DOWN the tree, but we need to move UP!

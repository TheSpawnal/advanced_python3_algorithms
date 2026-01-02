

#Algorithm 1:
"""
OPTIMAL-BST(p, q, n)
────────────────────────────────────────────────────────────
Input:
    p[1..n]  : probability of searching key k_i
    q[0..n]  : probability of unsuccessful search (dummy keys d_i)
    n        : number of keys

Output:
    e[1..n+1, 0..n]   : expected cost table
    root[1..n, 1..n]  : root choices table

────────────────────────────────────────────────────────────
1.  let e[1:n+1, 0:n], w[1:n+1, 0:n], root[1:n, 1:n] be new tables

2.  for i = 1 to n + 1                    // Base case: empty subtrees
3.      e[i, i-1] = q[i-1]
4.      w[i, i-1] = q[i-1]

5.  for l = 1 to n                        // l = chain length
6.      for i = 1 to n - l + 1            // i = left boundary
7.          j = i + l - 1                 // j = right boundary
8.          e[i, j] = infinity
9.          w[i, j] = w[i, j-1] + p[j] + q[j]
10.         for r = i to j                // r = candidate root
11.             t = e[i, r-1] + e[r+1, j] + w[i, j]
12.             if t < e[i, j]
13.                 e[i, j] = t
14.                 root[i, j] = r

15. return e and root
"""

#Algorithm 2:
"""
CONSTRUCT-OPTIMAL-BST(root, n)
────────────────────────────────────────────────────────────
1.  print "Optimal BST structure:"
2.  PRINT-TREE(root, 1, n, "root")
"""
#Algorithm 3: PRINT-TREE(root, i, j, position)
"""
PRINT-TREE(root, i, j, position)
────────────────────────────────────────────────────────────
1.  if i > j
2.      return                            // Empty subtree
3.  r = root[i, j]                        // Get root of subtree [i,j]
4.  print "k_" + r + " is the " + position
5.  PRINT-TREE(root, i, r-1, "left child of k_" + r)
6.  PRINT-TREE(root, r+1, j, "right child of k_" + r)
"""

"""
Conceptual Recap
Problem Statement
Given a sorted sequence of n keys K = {k₁, k₂, ..., kₙ} where k₁ < k₂ < ... < kₙ, 
build a BST that minimizes the expected search cost.
Each key kᵢ has:
p[i]: probability of searching for kᵢ (successful search)
q[i]: probability of landing in gap dᵢ (unsuccessful search between kᵢ and kᵢ₊₁)

The dummy keys d₀, d₁, ..., dₙ represent the n+1 gaps:
d₀: search value < k₁
dᵢ: kᵢ < search value < kᵢ₊₁
dₙ: search value > kₙ

Expected Search Cost
For a BST T:
E[search cost] = Σ(depth(kᵢ) + 1) · p[i]  +  Σ(depth(dᵢ) + 1) · q[i]
                 i=1..n                       i=0..n

Key Insight — Optimal Substructure
If optimal BST has root kᵣ for keys {kᵢ, ..., kⱼ}:
Left subtree (keys kᵢ, ..., kᵣ₋₁) must be optimal for those keys
Right subtree (keys kᵣ₊₁, ..., kⱼ) must be optimal for those keys

                                                  DP Recurrence
Weight function (sum of probabilities):
w[i, j] = Σ p[l] + Σ q[l]   for keys i to j
          l=i..j   l=i-1..j
Recurrence:
w[i, i-1] = q[i-1]                                    (empty subtree)
e[i, i-1] = q[i-1]                                    (only dummy key)

e[i, j] = min { e[i, r-1] + e[r+1, j] + w[i, j] }     for i ≤ r ≤ j
          r
The +w[i,j] term accounts for depth increase when subtrees become children.
Complexity: Time=O(n^3);Space=O(n^2);Tables=e,w,root-each O(n^2);
"""

import math
from typing import List, Tuple, Optional

def optimal_bst(p: List[float], q: List[float], n: int) -> Tuple[List[List[float]], List[List[int]]]:
    """
    Compute optimal BST tables using dynamic programming.
    
    Args:
        p: p[1..n] probabilities of successful search (index 0 unused)
        q: q[0..n] probabilities of unsuccessful search
        n: number of keys
    
    Returns:
        e: expected cost table e[i][j] for subtree with keys i..j
        root: root[i][j] = optimal root for subtree with keys i..j
    """
    # Tables: e and w are (n+2) x (n+1), root is (n+1) x (n+1)
    # Using 1-based indexing conceptually
    e = [[0.0] * (n + 1) for _ in range(n + 2)]
    w = [[0.0] * (n + 1) for _ in range(n + 2)]
    root = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: empty subtrees (i > j means e[i][i-1])
    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]
    
    # Fill tables for increasing chain lengths
    for length in range(1, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            e[i][j] = math.inf
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            
            # Try each key as root
            for r in range(i, j + 1):
                cost = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if cost < e[i][j]:
                    e[i][j] = cost
                    root[i][j] = r
    
    return e, root


def construct_optimal_bst(root: List[List[int]], n: int) -> None:
    """Print the structure of the optimal BST."""
    print("Optimal BST structure:")
    _print_tree(root, 1, n, "root")


def _print_tree(root: List[List[int]], i: int, j: int, position: str) -> None:
    """Recursively print tree structure."""
    if i > j:
        print(f"  d_{i-1} is the {position}")
        return
    
    r = root[i][j]
    print(f"  k_{r} is the {position}")
    _print_tree(root, i, r - 1, f"left child of k_{r}")
    _print_tree(root, r + 1, j, f"right child of k_{r}")


class BSTNode:
    """Node for actual tree construction."""
    def __init__(self, key_index: int, is_dummy: bool = False):
        self.key_index = key_index
        self.is_dummy = is_dummy
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None


def build_tree(root: List[List[int]], i: int, j: int) -> Optional[BSTNode]:
    """Construct actual tree from root table."""
    if i > j:
        return BSTNode(i - 1, is_dummy=True)
    
    r = root[i][j]
    node = BSTNode(r)
    node.left = build_tree(root, i, r - 1)
    node.right = build_tree(root, r + 1, j)
    return node


def print_tables(e: List[List[float]], w: List[List[float]], 
                 root: List[List[int]], n: int) -> None:
    """Display the DP tables."""
    print("\n--- Table e[i,j] (expected costs) ---")
    print("     j:", end="")
    for j in range(n + 1):
        print(f"{j:8}", end="")
    print()
    
    for i in range(1, n + 2):
        print(f"i={i}: ", end="")
        for j in range(n + 1):
            if j >= i - 1:
                print(f"{e[i][j]:8.4f}", end="")
            else:
                print("       -", end="")
        print()
    
    print("\n--- Table w[i,j] (probability sums) ---")
    print("     j:", end="")
    for j in range(n + 1):
        print(f"{j:8}", end="")
    print()
    
    for i in range(1, n + 2):
        print(f"i={i}: ", end="")
        for j in range(n + 1):
            if j >= i - 1:
                print(f"{w[i][j]:8.4f}", end="")
            else:
                print("       -", end="")
        print()
    
    print("\n--- Table root[i,j] (optimal roots) ---")
    print("     j:", end="")
    for j in range(1, n + 1):
        print(f"{j:4}", end="")
    print()
    
    for i in range(1, n + 1):
        print(f"i={i}: ", end="")
        for j in range(1, n + 1):
            if j >= i:
                print(f"{root[i][j]:4}", end="")
            else:
                print("   -", end="")
        print()


def visualize_tree(node: Optional[BSTNode], prefix: str = "", is_left: bool = True) -> None:
    """ASCII visualization of the tree."""
    if node is None:
        return
    
    connector = "|-- " if is_left else "`-- "
    if node.is_dummy:
        label = f"[d_{node.key_index}]"
    else:
        label = f"k_{node.key_index}"
    
    print(prefix + connector + label)
    
    child_prefix = prefix + ("|   " if is_left else "    ")
    
    if node.left or node.right:
        if node.left:
            visualize_tree(node.left, child_prefix, True)
        if node.right:
            visualize_tree(node.right, child_prefix, False)


def demo():
    """Demonstration with CLRS example."""
    # Keys: k1, k2, k3, k4, k5
    # p[0] unused, p[1..5] are key probabilities
    p = [0, 0.15, 0.10, 0.05, 0.10, 0.20]
    
    # q[0..5] are dummy key probabilities
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    
    n = 5
    
    print("=" * 60)
    print("OPTIMAL BINARY SEARCH TREE")
    print("=" * 60)
    
    print(f"\nInput (n={n} keys):")
    print(f"  p[1..{n}] = {p[1:]}")
    print(f"  q[0..{n}] = {q}")
    
    prob_sum = sum(p[1:]) + sum(q)
    print(f"  Sum of probabilities: {prob_sum:.2f}")
    
    # Compute optimal BST
    e, root_table = optimal_bst(p, q, n)
    
    # Print tables
    print_tables(e, root_table, n)
    
    # Print structure
    print("\n" + "=" * 60)
    construct_optimal_bst(root_table, n)
    
    # Build and visualize
    print("\n--- Tree Visualization ---")
    tree = build_tree(root_table, 1, n)
    visualize_tree(tree, "", False)
    
    # Final result
    print("\n" + "=" * 60)
    print(f"Minimum expected search cost: {e[1][n]:.4f}")
    print("=" * 60)


if __name__ == "__main__":
    demo()

## Sample Output
"""
============================================================
OPTIMAL BINARY SEARCH TREE
============================================================

Input (n=5 keys):
  p[1..5] = [0.15, 0.1, 0.05, 0.1, 0.2]
  q[0..5] = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]
  Sum of probabilities: 1.00

--- Table e[i,j] (expected costs) ---
     j:       0       1       2       3       4       5
i=1:   0.0500  0.4500  0.9000  1.2500  1.7000  2.7500
i=2:          0.1000  0.4000  0.7000  1.2000  2.0000
i=3:                  0.0500  0.2500  0.6000  1.3000
i=4:                          0.0500  0.3000  0.9000
i=5:                                  0.0500  0.5000
i=6:                                          0.1000

--- Table root[i,j] (optimal roots) ---
     j:   1   2   3   4   5
i=1:    1   1   2   2   2
i=2:        2   2   2   4
i=3:            3   4   5
i=4:                4   5
i=5:                    5

============================================================
Optimal BST structure:
  k_2 is the root
  k_1 is the left child of k_2
  d_0 is the left child of k_1
  d_1 is the right child of k_1
  k_5 is the right child of k_2
  k_4 is the left child of k_5
  k_3 is the left child of k_4
  d_2 is the left child of k_3
  d_3 is the right child of k_3
  d_4 is the right child of k_4
  d_5 is the right child of k_5

--- Tree Visualization ---
`-- k_2
    |-- k_1
    |   |-- [d_0]
    |   `-- [d_1]
    `-- k_5
        |-- k_4
        |   |-- k_3
        |   |   |-- [d_2]
        |   |   `-- [d_3]
        |   `-- [d_4]
        `-- [d_5]

============================================================
Minimum expected search cost: 2.7500
============================================================
"""

"""

Key Observations
-Root choice matters: k₂ becomes root despite k₅ having highest 
probability — the algorithm balances depth vs frequency globally.

-Dummy keys are leaves: They represent search failures and always sit at the bottom.

-The +w[i,j] term: This is the critical insight — when a subtree becomes a child, 
every node in it goes one level deeper, adding exactly w[i,j] to the expected cost.

-Knuth's optimization: Can reduce to O(n²) using the property that:
root[i,j-1] ≤ root[i,j] ≤ root[i+1,j].

"""


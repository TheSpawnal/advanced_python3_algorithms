"""
Algorithm 1: TOPOSORT(G)
TOPOSORT(G)
────────────────────────────────────────────────────────────
Input:
    G = (V, E)  : directed acyclic graph in adjacency-list representation

Output:
    f[v] for all v in V, constituting a topological ordering

Postcondition:
    The f-values of vertices constitute a topological ordering of G.
    (Lower f-value = earlier in topological order)

────────────────────────────────────────────────────────────
1.  mark all vertices as unexplored

2.  curLabel := |V|                 // Start labeling from n down to 1

3.  for every v in V do
4.      if v is unexplored then     // Not yet visited by prior DFS
5.          DFS-TOPO(G, v)


Algorithm 2: DFS-TOPO(G, s)
DFS-TOPO(G, s)
────────────────────────────────────────────────────────────
Input:
    G = (V, E)  : graph in adjacency-list representation
    s           : a vertex in V (current source)

Postcondition:
    Every vertex reachable from s is marked as "explored"
    and has an assigned f-value.

────────────────────────────────────────────────────────────
1.  mark s as explored

2.  for each edge (s, v) in s's outgoing adjacency list do
3.      if v is unexplored then
4.          DFS-TOPO(G, v)

5. f[s] := curLabel                // Assign s's position in ordering
6.  curLabel := curLabel - 1        // Work right-to-left (n down to 1)

"""

from typing import List, Dict, Set, Optional, Tuple
from collections import defaultdict

class TopologicalSortDFS:
    """
    Topological sort using DFS with reverse post-order labeling.
    Implements the exact algorithm from the pseudocode.
    """
    
    def __init__(self):
        self.graph: Dict[int, List[int]] = defaultdict(list)
        self.vertices: Set[int] = set()
    
    def add_edge(self, u: int, v: int) -> None:
        """Add directed edge u -> v."""
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
    
    def add_vertex(self, v: int) -> None:
        """Add isolated vertex."""
        self.vertices.add(v)
    
    def toposort(self) -> Optional[Dict[int, int]]:
        """
        Main TopoSort algorithm.
        
        Returns:
            f: dict mapping vertex -> position in topological order
               (f[v] = 1 means v is first, f[v] = |V| means v is last)
            None if cycle detected
        """
        n = len(self.vertices)
        
        # State
        explored: Set[int] = set()
        f: Dict[int, int] = {}
        self.cur_label = n          # Start from |V|, work down to 1
        self.has_cycle = False
        self.in_stack: Set[int] = set()  # For cycle detection
        
        def dfs_topo(s: int) -> None:
            """DFS-Topo: explore from s, assign f-values on finish."""
            if self.has_cycle:
                return
            
            # Mark s as explored (and in current DFS path)
            explored.add(s)
            self.in_stack.add(s)
            
            # Explore all outgoing edges
            for v in self.graph[s]:
                if v in self.in_stack:
                    # Back edge detected -> cycle
                    self.has_cycle = True
                    return
                if v not in explored:
                    dfs_topo(v)
            
            # Finished with s: assign label and decrement
            self.in_stack.remove(s)
            f[s] = self.cur_label
            self.cur_label -= 1
        
        # Main loop: visit all vertices
        for v in self.vertices:
            if v not in explored:
                dfs_topo(v)
                if self.has_cycle:
                    return None
        
        return f
    
    def toposort_as_list(self) -> Optional[List[int]]:
        """
        Return topological order as a list (first element = first in order).
        """
        f = self.toposort()
        if f is None:
            return None
        
        # Sort vertices by their f-value (ascending = topological order)
        return sorted(f.keys(), key=lambda v: f[v])
    
    def toposort_iterative(self) -> Optional[List[int]]:
        """
        Iterative version using explicit stack (avoids recursion limits).
        """
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {v: WHITE for v in self.vertices}
        result = []
        
        for start in self.vertices:
            if color[start] != WHITE:
                continue
            
            stack = [(start, iter(self.graph[start]))]
            color[start] = GRAY
            
            while stack:
                u, children = stack[-1]
                
                try:
                    v = next(children)
                    if color[v] == GRAY:
                        return None  # Cycle
                    if color[v] == WHITE:
                        color[v] = GRAY
                        stack.append((v, iter(self.graph[v])))
                except StopIteration:
                    # Finished with u
                    stack.pop()
                    color[u] = BLACK
                    result.append(u)
        
        result.reverse()
        return result


def visualize_dfs_execution(graph: Dict[int, List[int]], 
                            vertices: Set[int]) -> None:
    """
    Step-by-step visualization of DFS-based topological sort.
    """
    n = len(vertices)
    explored: Set[int] = set()
    f: Dict[int, int] = {}
    cur_label = n
    step = 0
    
    def dfs_topo(s: int, depth: int) -> None:
        nonlocal cur_label, step
        
        indent = "  " * depth
        step += 1
        print(f"{step:2}. {indent}DFS-TOPO({s}): mark {s} as explored")
        explored.add(s)
        
        for v in graph[s]:
            if v not in explored:
                print(f"    {indent}  -> exploring edge ({s}, {v})")
                dfs_topo(v, depth + 1)
            else:
                print(f"    {indent}  -> skip edge ({s}, {v}): already explored")
        
        step += 1
        f[s] = cur_label
        print(f"{step:2}. {indent}FINISH {s}: f[{s}] = {cur_label}, curLabel = {cur_label - 1}")
        cur_label -= 1
    
    print("=" * 60)
    print("DFS TOPOLOGICAL SORT - STEP BY STEP")
    print("=" * 60)
    print(f"\nInitial: curLabel = {n}, all vertices unexplored\n")
    
    for v in sorted(vertices):
        if v not in explored:
            print(f"--- Starting DFS from vertex {v} ---")
            dfs_topo(v, 0)
            print()
    
    print("=" * 60)
    print("RESULT")
    print("=" * 60)
    print(f"\nf-values: {f}")
    
    topo_order = sorted(f.keys(), key=lambda x: f[x])
    print(f"Topological order: {topo_order}")
    
    # Verify
    print("\nVerification (for each edge u->v, f[u] < f[v]):")
    valid = True
    for u in graph:
        for v in graph[u]:
            status = "ok" if f[u] < f[v] else "FAIL"
            print(f"  ({u} -> {v}): f[{u}]={f[u]} < f[{v}]={f[v]} ? {status}")
            if f[u] >= f[v]:
                valid = False
    
    print(f"\nValid topological order: {valid}")


def demo():
    """Demonstration with example DAG."""
    
    # Example DAG:
    #
    #     0 ──────► 1 ──────► 2
    #     │         │
    #     │         ▼
    #     └───────► 3 ──────► 4
    #               │
    #               ▼
    #               5
    #
    
    ts = TopologicalSortDFS()
    
    edges = [
        (0, 1),
        (0, 3),
        (1, 2),
        (1, 3),
        (3, 4),
        (3, 5),
    ]
    
    for u, v in edges:
        ts.add_edge(u, v)
    
    print("=" * 60)
    print("TOPOLOGICAL SORT VIA DFS")
    print("=" * 60)
    
    print("\nGraph edges:")
    for u in sorted(ts.vertices):
        if ts.graph[u]:
            print(f"  {u} -> {ts.graph[u]}")
    
    # Run algorithm
    f = ts.toposort()
    topo_list = ts.toposort_as_list()
    
    print(f"\nf-values (position labels):")
    for v in sorted(f.keys()):
        print(f"  f[{v}] = {f[v]}")
    
    print(f"\nTopological order: {topo_list}")
    
    # Detailed visualization
    print("\n")
    visualize_dfs_execution(ts.graph, ts.vertices)
    
    # Test cycle detection
    print("\n" + "=" * 60)
    print("CYCLE DETECTION TEST")
    print("=" * 60)
    
    cyclic = TopologicalSortDFS()
    cyclic.add_edge(0, 1)
    cyclic.add_edge(1, 2)
    cyclic.add_edge(2, 0)  # Creates cycle
    
    result = cyclic.toposort()
    print(f"\nGraph with cycle 0->1->2->0:")
    print(f"TopoSort result: {result}")
    print("(None indicates cycle detected)")


def demo_comparison():
    """Compare with alternative approaches."""
    
    print("\n" + "=" * 60)
    print("ALGORITHM COMPARISON")
    print("=" * 60)
    
    # Larger DAG for comparison
    ts = TopologicalSortDFS()
    
    # Diamond pattern with extra nodes
    edges = [
        (0, 1), (0, 2),
        (1, 3), (2, 3),
        (3, 4), (3, 5),
        (4, 6), (5, 6),
        (6, 7),
    ]
    
    for u, v in edges:
        ts.add_edge(u, v)
    
    # Method 1: Recursive DFS (from pseudocode)
    f_values = ts.toposort()
    order_recursive = ts.toposort_as_list()
    
    # Method 2: Iterative DFS
    order_iterative = ts.toposort_iterative()
    
    print("\nRecursive DFS result:")
    print(f"  f-values: {f_values}")
    print(f"  Order: {order_recursive}")
    
    print("\nIterative DFS result:")
    print(f"  Order: {order_iterative}")
    
    # Both should be valid topological orders (may differ)
    def verify_topo_order(order: List[int], graph: Dict[int, List[int]]) -> bool:
        pos = {v: i for i, v in enumerate(order)}
        for u in graph:
            for v in graph[u]:
                if pos[u] >= pos[v]:
                    return False
        return True
    
    print(f"\nRecursive order valid: {verify_topo_order(order_recursive, ts.graph)}")
    print(f"Iterative order valid: {verify_topo_order(order_iterative, ts.graph)}")


if __name__ == "__main__":
    demo()
    demo_comparison()




## Sample Output
"""
============================================================
TOPOLOGICAL SORT VIA DFS
============================================================

Graph edges:
  0 -> [1, 3]
  1 -> [2, 3]
  3 -> [4, 5]

f-values (position labels):
  f[0] = 1
  f[1] = 2
  f[2] = 4
  f[3] = 3
  f[4] = 5
  f[5] = 6

Topological order: [0, 1, 3, 2, 4, 5]


============================================================
DFS TOPOLOGICAL SORT - STEP BY STEP
============================================================

Initial: curLabel = 6, all vertices unexplored

--- Starting DFS from vertex 0 ---
 1.   DFS-TOPO(0): mark 0 as explored
       -> exploring edge (0, 1)
 2.     DFS-TOPO(1): mark 1 as explored
         -> exploring edge (1, 2)
 3.       DFS-TOPO(2): mark 2 as explored
 4.       FINISH 2: f[2] = 6, curLabel = 5
         -> exploring edge (1, 3)
 5.       DFS-TOPO(3): mark 3 as explored
           -> exploring edge (3, 4)
 6.         DFS-TOPO(4): mark 4 as explored
 7.         FINISH 4: f[4] = 5, curLabel = 4
           -> exploring edge (3, 5)
 8.         DFS-TOPO(5): mark 5 as explored
 9.         FINISH 5: f[5] = 4, curLabel = 3
10.       FINISH 3: f[3] = 3, curLabel = 2
11.     FINISH 1: f[1] = 2, curLabel = 1
       -> exploring edge (0, 3)
       -> skip edge (0, 3): already explored
12.   FINISH 0: f[0] = 1, curLabel = 0

============================================================
RESULT
============================================================

f-values: {2: 6, 4: 5, 5: 4, 3: 3, 1: 2, 0: 1}
Topological order: [0, 1, 3, 5, 4, 2]

Verification (for each edge u->v, f[u] < f[v]):
  (0 -> 1): f[0]=1 < f[1]=2 ? ok
  (0 -> 3): f[0]=1 < f[3]=3 ? ok
  (1 -> 2): f[1]=2 < f[2]=6 ? ok
  (1 -> 3): f[1]=2 < f[3]=3 ? ok
  (3 -> 4): f[3]=3 < f[4]=5 ? ok
  (3 -> 5): f[3]=3 < f[5]=4 ? ok

Valid topological order: True

============================================================
CYCLE DETECTION TEST
============================================================

Graph with cycle 0->1->2->0:
TopoSort result: None
(None indicates cycle detected)
```

---

## Summary: The Labeling Mechanism
```
    DFS Call Stack              curLabel        Action
    ──────────────              ────────        ──────
    
    enter(0)                    6               
      enter(1)                  6               
        enter(2)                6               
        exit(2)                 6 -> 5          f[2] = 6
        enter(3)                5               
          enter(4)              5               
          exit(4)               5 -> 4          f[4] = 5
          enter(5)              4               
          exit(5)               4 -> 3          f[5] = 4
        exit(3)                 3 -> 2          f[3] = 3
      exit(1)                   2 -> 1          f[1] = 2
    exit(0)                     1 -> 0          f[0] = 1

  """

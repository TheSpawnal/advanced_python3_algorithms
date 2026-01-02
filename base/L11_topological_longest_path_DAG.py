

'''
- You are given a directed acyclic graph with real-valued edge 
weights and two distinguished vertices s and t. 
Describe a dynamic-programming approach for finding a longest weighted 
simple path from s to t.  
- What is the running time of your algorithm?



'''


from collections import deque, defaultdict
from typing import List, Dict, Tuple, Optional
import math

class DAGLongestPath:
    """Longest path in DAG using topological ordering + DP."""
    
    def __init__(self):
        self.graph: Dict[int, List[Tuple[int, float]]] = defaultdict(list)
        self.vertices: set = set()
    
    def add_edge(self, u: int, v: int, weight: float) -> None:
        """Add directed edge u -> v with given weight."""
        self.graph[u].append((v, weight))
        self.vertices.add(u)
        self.vertices.add(v)
    
    def topological_sort_kahn(self) -> Optional[List[int]]:
        """Kahn's algorithm: BFS-based topological sort."""
        in_degree = defaultdict(int)
        
        for v in self.vertices:
            if v not in in_degree:
                in_degree[v] = 0
        
        for u in self.graph:
            for v, _ in self.graph[u]:
                in_degree[v] += 1
        
        queue = deque([v for v in self.vertices if in_degree[v] == 0])
        result = []
        
        while queue:
            u = queue.popleft()
            result.append(u)
            
            for v, _ in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        if len(result) != len(self.vertices):
            return None  # Cycle detected
        
        return result
    
    def topological_sort_dfs(self) -> Optional[List[int]]:
        """DFS-based topological sort."""
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {v: WHITE for v in self.vertices}
        result = []
        has_cycle = False
        
        def dfs(u: int) -> None:
            nonlocal has_cycle
            if has_cycle:
                return
            
            color[u] = GRAY
            
            for v, _ in self.graph[u]:
                if color[v] == GRAY:
                    has_cycle = True
                    return
                if color[v] == WHITE:
                    dfs(v)
            
            color[u] = BLACK
            result.append(u)
        
        for v in self.vertices:
            if color[v] == WHITE:
                dfs(v)
        
        if has_cycle:
            return None
        
        result.reverse()
        return result
    
    def longest_path(self, s: int, t: int, 
                     use_dfs_topo: bool = False) -> Tuple[float, List[int]]:
        """
        Find longest path from s to t.
        
        Returns:
            (distance, path) where path is list of vertices,
            or (-inf, []) if no path exists
        """
        # Step 1: Topological sort
        if use_dfs_topo:
            topo_order = self.topological_sort_dfs()
        else:
            topo_order = self.topological_sort_kahn()
        
        if topo_order is None:
            raise ValueError("Graph contains a cycle - not a DAG")
        
        # Step 2: Initialize
        d = {v: -math.inf for v in self.vertices}
        pi = {v: None for v in self.vertices}
        d[s] = 0
        
        # Step 3: Relax in topological order
        for u in topo_order:
            if d[u] != -math.inf:  # u is reachable from s
                for v, weight in self.graph[u]:
                    if d[u] + weight > d[v]:
                        d[v] = d[u] + weight
                        pi[v] = u
        
        # Step 4: Reconstruct path
        if d[t] == -math.inf:
            return -math.inf, []
        
        path = []
        current = t
        while current is not None:
            path.append(current)
            current = pi[current]
        path.reverse()
        
        return d[t], path
    
    def shortest_path(self, s: int, t: int) -> Tuple[float, List[int]]:
        """
        For comparison: shortest path (same structure, different relaxation).
        """
        topo_order = self.topological_sort_kahn()
        
        if topo_order is None:
            raise ValueError("Graph contains a cycle")
        
        d = {v: math.inf for v in self.vertices}
        pi = {v: None for v in self.vertices}
        d[s] = 0
        
        for u in topo_order:
            if d[u] != math.inf:
                for v, weight in self.graph[u]:
                    if d[u] + weight < d[v]:  # Minimize instead
                        d[v] = d[u] + weight
                        pi[v] = u
        
        if d[t] == math.inf:
            return math.inf, []
        
        path = []
        current = t
        while current is not None:
            path.append(current)
            current = pi[current]
        path.reverse()
        
        return d[t], path
    
    def all_longest_paths_from(self, s: int) -> Dict[int, Tuple[float, List[int]]]:
        """Compute longest paths from s to all reachable vertices."""
        topo_order = self.topological_sort_kahn()
        
        d = {v: -math.inf for v in self.vertices}
        pi = {v: None for v in self.vertices}
        d[s] = 0
        
        for u in topo_order:
            if d[u] != -math.inf:
                for v, weight in self.graph[u]:
                    if d[u] + weight > d[v]:
                        d[v] = d[u] + weight
                        pi[v] = u
        
        # Reconstruct all paths
        result = {}
        for v in self.vertices:
            if d[v] != -math.inf:
                path = []
                current = v
                while current is not None:
                    path.append(current)
                    current = pi[current]
                path.reverse()
                result[v] = (d[v], path)
        
        return result


def print_graph(dag: DAGLongestPath) -> None:
    """Display adjacency list."""
    print("Graph (adjacency list):")
    for u in sorted(dag.vertices):
        edges = dag.graph[u]
        if edges:
            edge_str = ", ".join(f"{v}(w={w})" for v, w in edges)
            print(f"  {u} -> {edge_str}")
        else:
            print(f"  {u} -> (no outgoing edges)")


def demo():
    """Demonstration with example DAG."""
    dag = DAGLongestPath()
    
    # Build example DAG
    #
    #     2       3
    # 0 ────► 1 ────► 3
    # │       │       ▲
    # │4      │1      │2
    # ▼       ▼       │
    # 2 ────► 4 ──────┘
    #     3
    #
    edges = [
        (0, 1, 2),
        (0, 2, 4),
        (1, 3, 3),
        (1, 4, 1),
        (2, 4, 3),
        (4, 3, 2),
    ]
    
    for u, v, w in edges:
        dag.add_edge(u, v, w)
    
    print("=" * 60)
    print("LONGEST PATH IN DAG")
    print("=" * 60)
    
    print_graph(dag)
    
    # Topological sort
    topo_kahn = dag.topological_sort_kahn()
    topo_dfs = dag.topological_sort_dfs()
    
    print(f"\nTopological order (Kahn): {topo_kahn}")
    print(f"Topological order (DFS):  {topo_dfs}")
    
    # Longest path
    s, t = 0, 3
    print(f"\n--- Longest Path from {s} to {t} ---")
    
    dist, path = dag.longest_path(s, t)
    print(f"Distance: {dist}")
    print(f"Path: {' -> '.join(map(str, path))}")
    
    # Shortest path for comparison
    print(f"\n--- Shortest Path from {s} to {t} ---")
    
    dist_short, path_short = dag.shortest_path(s, t)
    print(f"Distance: {dist_short}")
    print(f"Path: {' -> '.join(map(str, path_short))}")
    
    # All longest paths from source
    print(f"\n--- All Longest Paths from {s} ---")
    all_paths = dag.all_longest_paths_from(s)
    
    for v in sorted(all_paths.keys()):
        d, p = all_paths[v]
        print(f"  to {v}: dist={d:5.1f}, path={' -> '.join(map(str, p))}")
    
    # Edge case: unreachable target
    print("\n--- Unreachable Target Test ---")
    dag.add_edge(5, 6, 10)  # Disconnected component
    dist_none, path_none = dag.longest_path(0, 6)
    print(f"Path from 0 to 6: dist={dist_none}, path={path_none}")
    
    print("\n" + "=" * 60)


def demo_critical_path():
    """
    Critical path method: classic application of longest path in DAG.
    Project scheduling with task dependencies.
    """
    print("\n" + "=" * 60)
    print("CRITICAL PATH METHOD (CPM)")
    print("=" * 60)
    
    # Tasks with durations and dependencies
    # Task: (duration, [dependencies])
    tasks = {
        'A': (3, []),           # Start task
        'B': (4, ['A']),
        'C': (2, ['A']),
        'D': (5, ['B']),
        'E': (3, ['B', 'C']),
        'F': (2, ['D', 'E']),   # End task
    }
    
    # Build DAG with task durations as edge weights
    dag = DAGLongestPath()
    
    # Add virtual start (node 0) and end (node -1)
    task_to_id = {name: i+1 for i, name in enumerate(tasks.keys())}
    task_to_id['START'] = 0
    task_to_id['END'] = len(tasks) + 1
    id_to_task = {v: k for k, v in task_to_id.items()}
    
    # Connect start to tasks with no dependencies
    for task, (duration, deps) in tasks.items():
        if not deps:
            dag.add_edge(task_to_id['START'], task_to_id[task], 0)
    
    # Connect tasks based on dependencies
    for task, (duration, deps) in tasks.items():
        for dep in deps:
            dep_duration = tasks[dep][0]
            dag.add_edge(task_to_id[dep], task_to_id[task], dep_duration)
    
    # Connect final tasks to end
    end_tasks = ['F']  # Tasks with no successors
    for task in end_tasks:
        dag.add_edge(task_to_id[task], task_to_id['END'], tasks[task][0])
    
    print("\nProject tasks:")
    for task, (duration, deps) in tasks.items():
        dep_str = ', '.join(deps) if deps else 'none'
        print(f"  {task}: duration={duration}, depends on: {dep_str}")
    
    # Find critical path
    dist, path = dag.longest_path(task_to_id['START'], task_to_id['END'])
    
    critical_tasks = [id_to_task[p] for p in path]
    
    print(f"\nCritical path: {' -> '.join(critical_tasks)}")
    print(f"Minimum project duration: {dist}")
    print("\nCritical tasks cannot be delayed without delaying the project.")


if __name__ == "__main__":
    demo()
    demo_critical_path()


## Sample Output
"""
============================================================
LONGEST PATH IN DAG
============================================================
Graph (adjacency list):
  0 -> 1(w=2), 2(w=4)
  1 -> 3(w=3), 4(w=1)
  2 -> 4(w=3)
  3 -> (no outgoing edges)
  4 -> 3(w=2)

Topological order (Kahn): [0, 1, 2, 4, 3]
Topological order (DFS):  [0, 2, 1, 4, 3]

--- Longest Path from 0 to 3 ---
Distance: 9.0
Path: 0 -> 2 -> 4 -> 3

--- Shortest Path from 0 to 3 ---
Distance: 5.0
Path: 0 -> 1 -> 3

--- All Longest Paths from 0 ---
  to 0: dist=  0.0, path=0
  to 1: dist=  2.0, path=0 -> 1
  to 2: dist=  4.0, path=0 -> 2
  to 3: dist=  9.0, path=0 -> 2 -> 4 -> 3
  to 4: dist=  7.0, path=0 -> 2 -> 4

--- Unreachable Target Test ---
Path from 0 to 6: dist=-inf, path=[]

============================================================

============================================================
CRITICAL PATH METHOD (CPM)
============================================================

Project tasks:
  A: duration=3, depends on: none
  B: duration=4, depends on: A
  C: duration=2, depends on: A
  D: duration=5, depends on: B
  E: duration=3, depends on: B, C
  F: duration=2, depends on: D, E

Critical path: START -> A -> B -> D -> F -> END
Minimum project duration: 14.0

Critical tasks cannot be delayed without delaying the project.

"""


'''
Summary Table
Aspect:            Detail:
Problem            Longest simple path s → t in weighted DAG
Approach           Topological sort + DP relaxation
Time                O(V + E)
Space                O(V + E)
Key insight            Topo-order ensures all predecessors processed first
General graphs          NP-hard (no polynomial solution known)
Applications            Critical path, scheduling, dependency resolution

The acyclic property transforms an intractable problem into a linear-time 
solution — one of the cleanest examples of structure enabling efficiency in algorithm design.
'''

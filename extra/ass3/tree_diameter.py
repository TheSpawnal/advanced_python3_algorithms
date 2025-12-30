

from collections import deque


def bfs_farthest(adj_list: dict, source: int) -> tuple[int, int, dict]:
    """
    BFS from source node to find farthest node.
    
    Returns:
        (farthest_node, max_distance, distances_dict)
    """
    distances = {node: -1 for node in adj_list}
    parent = {node: None for node in adj_list}
    
    queue = deque([source])
    distances[source] = 0
    
    while queue:
        current = queue.popleft()
        for neighbor in adj_list[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)
    
    farthest_node = max(distances, key=lambda x: distances[x])
    max_distance = distances[farthest_node]
    
    return farthest_node, max_distance, parent


def compute_diameter(adj_list: dict) -> tuple[int, list]:
    """
    Compute tree diameter using two BFS passes.
    
    Returns:
        (diameter_length, diameter_path)
    """
    if not adj_list:
        return 0, []
    
    if len(adj_list) == 1:
        return 0, [list(adj_list.keys())[0]]
    
    start_node = next(iter(adj_list))
    
    endpoint_u, _, _ = bfs_farthest(adj_list, start_node)
    endpoint_v, diameter, parent = bfs_farthest(adj_list, endpoint_u)
    
    path = []
    current = endpoint_v
    while current is not None:
        path.append(current)
        current = parent[current]
    
    return diameter, path


def build_adjacency_list(edges: list[tuple[int, int]]) -> dict:
    """Build adjacency list from edge list."""
    adj = {}
    for u, v in edges:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)
    return adj


def run_test(name: str, edges: list[tuple[int, int]]):
    """Run diameter computation on a test case."""
    print(f"Test: {name}")
    print(f"Edges: {edges}")
    
    adj_list = build_adjacency_list(edges)
    diameter, path = compute_diameter(adj_list)
    
    print(f"Diameter: {diameter}")
    print(f"Path: {' -> '.join(map(str, path))}")
    print(f"Endpoints: {path[0]}, {path[-1]}")
    print()


if __name__ == "__main__":
    
    # Test 1: Linear chain
    # 0 - 1 - 2 - 3 - 4
    run_test(
        "Linear chain (5 nodes)",
        [(0, 1), (1, 2), (2, 3), (3, 4)]
    )
    
    # Test 2: Star graph
    #     1
    #     |
    # 2 - 0 - 3
    #     |
    #     4
    run_test(
        "Star graph (hub at 0)",
        [(0, 1), (0, 2), (0, 3), (0, 4)]
    )
    
    # Test 3: Binary tree
    #        0
    #       / \
    #      1   2
    #     / \   \
    #    3   4   5
    run_test(
        "Binary tree",
        [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
    )
    
    # Test 4: Example from explanation
    #        0
    #       / \
    #      1   2
    #     / \   \
    #    3   4   5
    #   /
    #  6
    run_test(
        "Tree from explanation",
        [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (3, 6)]
    )
    
    # Test 5: Longer unbalanced tree
    #  0 - 1 - 2 - 3
    #      |
    #      4 - 5 - 6 - 7 - 8
    run_test(
        "Unbalanced tree",
        [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
    )
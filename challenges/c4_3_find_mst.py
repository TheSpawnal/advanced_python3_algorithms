

"""
Find the minimum spanning tree in the graph on the input. 
Based on the minimum spanning tree you can make a recommendation for the urban planning project 
about which roads (edges) are good candidates for removal and which are absolutely 
essential on the road and should not be considered in the future plans of construction changes.
 Dataformat3. The min_spanning_tree functiontakesthesameparameters asTask2.
 The function returns the list of edges of the minimum spanning tree, ordered by cost.
 [(<id1,1>, <id1,2>, <cost1>), ..., (<idm,1>, <idm,2>, <costm>)]
"""


from typing import List, Tuple

class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return False

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

        return True

def min_spanning_tree(nodes_l: List[int],
                      edges_l: List[Tuple[int, int, int]]
                      ) -> List[Tuple[int, int, int]]:
    '''
    Find the minimum spanning tree

    ### Parameters
    `nodes_l`: List of `integer` graph nodes
    `edges_l`: List of the edges of the graph and their cost as `tuples`
        e.g. `[(u1, v1, cost1), (u2, v2, cost2), ...]`

    ### Return
    The edges of the minimum spanning tree and their weight,
        same format as `edges_l`.

        The order of the return list does not matter:
            e.g. `[(u1,v1,c1), (u2,v2,c2)] == [(u2,v2,c2), (u1,v1,c1)]`
        As an undirected graph, the *direction* of the edges does not matter:
            e.g. `[(u, v, c)] == [(v, u, c)]`
    '''

    # Sort edges by cost
    sorted_edges = sorted(edges_l, key=lambda x: x[2])

    # Initialize UnionFind data structure
    uf = UnionFind(nodes_l)

    mst = []
    for u, v, cost in sorted_edges:
        if uf.union(u, v):
            mst.append((u, v, cost))

        # If we've added n-1 edges, we're done
        if len(mst) == len(nodes_l) - 1:
            break

    return mst

# Example usage
if __name__ == "__main__":
    nodes = [0, 1, 2, 3, 4]
    edges = [
        (0, 1, 10), (0, 2, 6), (0, 3, 5),
        (1, 3, 15), (2, 3, 4),
        (3, 4, 8), (2, 4, 3)
    ]

    mst = min_spanning_tree(nodes, edges)
    
    print("Minimum Spanning Tree edges:")
    for u, v, cost in mst:
        print(f"Edge ({u}, {v}) with cost {cost}")
    
    print("\nRecommendations for urban planning:")
    print("Essential roads (should not be removed):")
    for u, v, cost in mst:
        print(f"  Road between nodes {u} and {v}")
    
    print("\nRoads that could potentially be removed:")
    for u, v, cost in edges:
        if (u, v, cost) not in mst and (v, u, cost) not in mst:
            print(f"  Road between nodes {u} and {v}")

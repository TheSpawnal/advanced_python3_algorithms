
'''
ShortestPath
we will develop an algorithm that finds the shortest path between a user 
(TwitterID-A) spreading fake news and some other user(TwitterID-B).
Allowed data structures 3: tuple, dict, list, set

Dataformat3. The shortest_path function takes three parameters: 
two integers representing the start and end node ids, and, 
the list of the twitter users with their number of likes and the 
users they arefollowing. Each twitter user(node)is given as a 
tuple(tuple[id:int, num_likes:int, following:list[int]]).

All edges directed to a nodeu have a weight of 1/num_likes u
[ (<id1>, <num_likes1>, [<id1,1>, <id1,2>, ...]), ..., (<idn>, <num_likesn>,
[<idn,1>, <idn,2>, ...]) ]
The function returns a list of integer node_ids of the shortest paths between the start and end nodes.
[<idstart, ..., <idend>]
Call: shortest_path(1, 3, [(1, 2, [2, 3]), (2, 5, [3, 1]), (3, 6, [2])])
Returns (list[int]): [1, 3]
'''



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
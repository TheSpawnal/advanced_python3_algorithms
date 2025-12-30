

"""
pseudo code

input: a set x of data points, a symmetric similarity
function f, and a positive integer k ∈ {1,2,3,....,|X|}
output: a partition of X into k non-empty clusters

C:= NULL //keeps track of current clusters
for each x ∈ X do
    Add{x} to C

//main loop
while C contains more than k cluster do
    remove from C the clusters S_1, S_2 that minimize 
    F(S_1, S_2)
    add S_1 Union S_2 to C
return C



● Important in unsupervised ML
● Goal = partition data into “coherent groups” / clusters
● Similarity function f(x,y) = symmetric, assigns a similarity 
score to pair data points x,y
● F(S_1,S_2)=min f(x,y), where x∈S_1 and y∈S_2 or “best case” 
similarity between points in different clusters
"""





from typing import List, Tuple, Callable
import heapq

class UnionFind:
    def __init__(self, elements):
        self.parent = {x: x for x in elements}
        self.rank = {x: 0 for x in elements}

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

def single_link_clustering(X: List, f: Callable[[any, any], float], k: int) -> List[List]:
    """
    Perform single-link clustering on a set of data points.

    Args:
    X (List): A list of data points.
    f (Callable[[any, any], float]): A symmetric similarity function.
    k (int): The desired number of clusters.

    Returns:
    List[List]: A list of k clusters, where each cluster is a list of data points.
    """
    n = len(X)
    if k < 1 or k > n:
        raise ValueError("k must be between 1 and the number of data points")

    # Calculate pairwise similarities and sort
    similarities = []
    for i in range(n):
        for j in range(i + 1, n):
            similarity = f(X[i], X[j])
            similarities.append((-similarity, i, j))  # Negative for max-heap behavior

    heapq.heapify(similarities)

    # Initialize UnionFind data structure
    uf = UnionFind(range(n))
    num_clusters = n

    # Main clustering loop
    while num_clusters > k and similarities:
        _, i, j = heapq.heappop(similarities)
        if uf.union(i, j):
            num_clusters -= 1

    # Collect clusters
    clusters = {}
    for i in range(n):
        root = uf.find(i)
        if root not in clusters:
            clusters[root] = []
        clusters[root].append(X[i])

    return list(clusters.values())

# Example usage
if __name__ == "__main__":
    # Example data points (2D coordinates)
    X = [(1, 2), (2, 1), (2, 3), (3, 2), (8, 7), (8, 8), (7, 8), (9, 9)]

    # Example similarity function (negative Euclidean distance)
    def similarity(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
        return -((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

    k = 2  # Desired number of clusters

    clusters = single_link_clustering(X, similarity, k)

    print(f"Clustered {len(X)} points into {k} clusters:")
    for i, cluster in enumerate(clusters, 1):
        print(f"Cluster {i}: {cluster}")
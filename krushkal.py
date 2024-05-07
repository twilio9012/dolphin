class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def kruskal_mst(self):
        mst = []
        total_cost = 0

        self.graph.sort(key=lambda x: x[2])

        ds = DisjointSet(range(1, self.V + 1))  # Handle 1-indexed vertices

        for edge in self.graph:
            u, v, w = edge
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                mst.append((u, v, w))
                total_cost += w

        return mst, total_cost

# User input for the graph
V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))
g = Graph(V)

print("Enter the details of each edge (source, destination, weight):")
for _ in range(E):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

# Calculate Minimum Spanning Tree
mst, total_cost = g.kruskal_mst()

# Output Minimum Spanning Tree and total cost
print("\nMinimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total cost:", total_cost)


"""
Enter the number of vertices: 5
Enter the number of edges: 7
Enter the details of each edge (source, destination, weight):
1 2 7
1 4 8
2 3 5
4 5 3
4 3 6
3 5 2
2 4 3

Minimum Spanning Tree:
(3, 5, 2)
(4, 5, 3)
(2, 4, 3)
(1, 2, 7)
Total cost: 15




This code implements Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a weighted, undirected graph. Let's break down the code step by step:

1. **DisjointSet class**:
   - This class represents a disjoint-set data structure, which is used to efficiently implement the union-find algorithm.
   - `__init__`: Initializes the disjoint-set with a given list of vertices. Each vertex is initially its own parent, and the rank of each vertex is set to 0.
   - `find`: Finds the representative (root) of the set containing the vertex `v`. It utilizes path compression to optimize subsequent find operations.
   - `union`: Merges the sets containing vertices `u` and `v`. It compares the ranks of the sets and performs union by rank to maintain the efficiency of the data structure.

2. **Graph class**:
   - This class represents a graph.
   - `__init__`: Initializes the graph with a given number of vertices.
   - `add_edge`: Adds an edge to the graph with its source vertex `u`, destination vertex `v`, and weight `w`.

3. **kruskal_mst method**:
   - This method implements Kruskal's algorithm to find the Minimum Spanning Tree (MST) of the graph.
   - It sorts the edges of the graph based on their weights in non-decreasing order.
   - It initializes an empty MST and a total cost counter.
   - It creates a disjoint-set data structure to keep track of connected components.
   - It iterates through the sorted edges and adds each edge to the MST if adding it does not create a cycle (i.e., the source and destination vertices belong to different sets in the disjoint-set data structure). If the edge is added, its weight is added to the total cost.
   - Finally, it returns the MST and the total cost.

4. **User input and MST calculation**:
   - The user is prompted to enter the number of vertices (`V`) and the number of edges (`E`) in the graph.
   - For each edge, the user inputs the source vertex, destination vertex, and weight.
   - The MST is calculated using Kruskal's algorithm (`kruskal_mst` method).

5. **Output**:
   - The code outputs the edges of the Minimum Spanning Tree and the total cost of the MST.
"""

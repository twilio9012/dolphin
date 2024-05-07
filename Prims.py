def minKey(key, mstSet):
    min = float('inf')
    minIndex = -1

    for i in range(len(key)):
        if not mstSet[i] and key[i] < min:
            min = key[i]
            minIndex = i

    return minIndex


def printMST(parent, graph,sum):
    print("Edge \tWeight")
    for i in range(1, len(parent)):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])
    print("Minimum weight of MST:", sum)

def prim(graph, numVertices):
    parent = [0] * numVertices
    key = [float('inf')] * numVertices
    mstSet = [False] * numVertices

    key[0] = 0
    parent[0] = -1

    for count in range(numVertices - 1):
        u = minKey(key, mstSet)
        mstSet[u] = True

        for v in range(numVertices):
            if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    sum = 0
    for i in range(numVertices):
        sum += key[i]

    printMST(parent, graph, sum)


n = int(input("Enter the size of the graph: "))
graph = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        graph[i][j] = int(input("Enter the weight {}->{} of the graph: ".format(i, j)))

prim(graph, n)

"""
Enter the size of the graph: 5
Enter the weight 0->0 of the graph: 0
Enter the weight 0->1 of the graph: 7
Enter the weight 0->2 of the graph: 8
Enter the weight 0->3 of the graph: 0
Enter the weight 0->4 of the graph: 0
Enter the weight 1->0 of the graph: 7
Enter the weight 1->1 of the graph: 0
Enter the weight 1->2 of the graph: 3
Enter the weight 1->3 of the graph: 6
Enter the weight 1->4 of the graph: 0
Enter the weight 2->0 of the graph: 8
Enter the weight 2->1 of the graph: 3
Enter the weight 2->2 of the graph: 0
Enter the weight 2->3 of the graph: 4
Enter the weight 2->4 of the graph: 3
Enter the weight 3->0 of the graph: 0
Enter the weight 3->1 of the graph: 6
Enter the weight 3->2 of the graph: 4
Enter the weight 3->3 of the graph: 0
Enter the weight 3->4 of the graph: 2
Enter the weight 4->0 of the graph: 0
Enter the weight 4->1 of the graph: 0
Enter the weight 4->2 of the graph: 3
Enter the weight 4->3 of the graph: 2
Enter the weight 4->4 of the graph: 0
Edge 	Weight
0 - 1 	 7
1 - 2 	 3
4 - 3 	 2
2 - 4 	 3
Minimum weight of MST: 15








Sure, let's break down the code step by step:

1. **minKey(key, mstSet)**:
   - This function is used to find the vertex with the minimum key value that is not yet included in the Minimum Spanning Tree (MST).
   - Parameters:
     - `key`: A list containing the key values for each vertex.
     - `mstSet`: A boolean list indicating whether a vertex is already included in the MST.
   - It iterates over each vertex and checks if it is not in the MST (`not mstSet[i]`) and if its key value is smaller than the current minimum (`key[i] < min`). If both conditions are met, it updates the minimum value and its index.
   - Finally, it returns the index of the vertex with the minimum key value.

2. **printMST(parent, graph, sum)**:
   - This function prints the MST and its total weight.
   - Parameters:
     - `parent`: A list representing the parent of each vertex in the MST.
     - `graph`: The adjacency matrix representation of the graph.
     - `sum`: The total weight of the MST.
   - It iterates over each vertex (excluding the root vertex at index 0) and prints the edge (parent-child) and its weight.
   - Finally, it prints the total weight of the MST.

3. **prim(graph, numVertices)**:
   - This is the main function that implements Prim's algorithm to find the Minimum Spanning Tree (MST).
   - Parameters:
     - `graph`: The adjacency matrix representation of the graph.
     - `numVertices`: The number of vertices in the graph.
   - It initializes three lists:
     - `parent`: To store the parent of each vertex in the MST.
     - `key`: To store the key values of each vertex. Initialized with infinity.
     - `mstSet`: To keep track of vertices included in the MST. Initialized as False for all vertices.
   - It starts by setting the key value of the root vertex (0) to 0.
   - Then, it iterates `numVertices - 1` times to find the MST.
     - In each iteration, it finds the vertex `u` with the minimum key value using the `minKey` function.
     - It marks `u` as included in the MST (`mstSet[u] = True`).
     - It updates the key values and parent vertices of the adjacent vertices of `u`, if they are not already included in the MST and if the weight of the edge to them is smaller than their current key value.
   - After constructing the MST, it calculates the total weight of the MST and prints the MST using the `printMST` function.

4. **User Input**:
   - The user is prompted to enter the size of the graph (`n`) and then the weights of the edges between vertices.

5. **Execution**:
   - Finally, the `prim` function is called with the input graph and its size.


"""

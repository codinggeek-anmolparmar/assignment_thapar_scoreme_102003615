
### 2. `main.py`

```python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""
def longest_path(graph: list) -> int:
    # Your implementation goes here
    #calculate number of nodes in the graph
    n = len(graph)
    #calculating topological order
    topo_order = topological_sort(graph)
    #finding longest path 
    return calculate_longest_path(graph, topo_order, n)
    

# Helper function to perform topological sort
def topological_sort(graph):
    n = len(graph)
    in_degree = [0] * n
    for u in range(n):
        for v, _ in graph[u]:
            in_degree[v] += 1
            
    zero_in_degree = [u for u in range(n) if in_degree[u] == 0]
    topo_order = []
    
    while zero_in_degree:
        u = zero_in_degree.pop()
        topo_order.append(u)
        for v, _ in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                zero_in_degree.append(v)
                
    return topo_order

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order,n):
    dist = [-float('inf')] * n
    for u in topo_order:
        if dist[u] == -float('inf'):
            dist[u] = 0
        for v, w in graph[u]:
            if dist[v] < dist[u] + w:
                dist[v] = dist[u] + w
    
    return max(dist)

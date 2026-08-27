from collections import deque


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

    return visited


bfs_path = bfs(graph, 'A')
dfs_path = dfs(graph, 'A')


print("BFS Traversal:", bfs_path)
print("DFS Traversal:", dfs_path)

print("\nComparison:")
print("BFS Time Complexity  : O(V + E)")
print("DFS Time Complexity  : O(V + E)")
print("BFS Space Complexity : O(V)")
print("DFS Space Complexity : O(V)")
from collections import deque
def bfs(graph, start):
    queue, visited = deque([start]), set()
    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    print()
graph = {
    'A': ['C', 'B'],   
    'B': ['A', 'E', 'D'], 
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting from A
bfs(graph, 'A')

from collections import deque
def dfs(graph, start):
    stack, visited = [start], set()
    print("DFS Traversal:", end=" ")
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed([neighbor for neighbor in graph[node] if neighbor not in visited]))
    print()

graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6'],
    '4': ['2', '7'],
    '5': ['2', '6'],
    '6': ['3', '5'],
    '7': ['4']
}
dfs(graph, '1')

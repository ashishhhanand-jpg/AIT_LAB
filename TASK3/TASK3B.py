# Corrected A* Algorithm

# Define the neighbors for each node
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('G', 9)],
    'C': [('B', 1), ('F', 3)],
    'D': [('E', 6), ('G', 1)],
    'E': [('A', 3), ('D', 6)],
    'F': [('C', 3), ('G', 2)],
    'G': [('B', 9), ('D', 1), ('F', 2)]
}

# Heuristic distances to goal node 'G'
def heuristic(n):
    h_dist = {
        'A': 5,
        'B': 3,
        'C': 4,
        'D': 1,
        'E': 2,
        'F': 2,
        'G': 0  # Goal node
    }
    return h_dist[n]

# Function to return neighbors and their distances
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    return None

# A* Algorithm
def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}  # distance from start node
    parents = {}  # parent nodes for path reconstruction

    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        # Find node with lowest f() = g + h
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or n is None or n not in Graph_nodes:
            break

        for m, weight in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    # Reconstruct path
    if n == stop_node:
        path = []
        while parents[n] != n:
            path.append(n)
            n = parents[n]
        path.append(start_node)
        path.reverse()
        print('Path found:', path)
        return path

    print('Path does not exist!')
    return None

# Run A* from 'A' to 'G'
print("Following is the A* Algorithm:")
aStarAlgo('A', 'G')

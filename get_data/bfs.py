

# this is implementation for BFS ALgorithm

def BFS(start, goal, getData, getGraph):
    graph = getGraph.get_graph_values(getData)
    queue = [(start, [start])]
    visited = set()

    while queue:
        current_node, path = queue.pop(0)

        if current_node == goal:
            return path  # Return the path if the goal is reached

        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return None  # No path found

# print(BFS("Jerusalem", "Rafah"))
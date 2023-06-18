import heapq


# this is implementation for A* start Alogrithm

def AStar(start, goal, getData, getGraph):
    
    graph = getGraph.get_edges_with_values(getData)
    heuristic = getData.get_heuristic_data(goal)
    
    queue = []
    visited = set()
    
    
    # Push the start node to the priority queue with priority 0
    heapq.heappush(queue, (0, start))
    # Initialize the cost dictionary
    cost = {start: 0}
    # Initialize the path dictionary
    path = {start: None}

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if current_node == goal:
            # Reached the goal node, reconstruct and return the path
            return reconstruct_path(path, goal)

        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            new_cost = cost[current_node] + float(graph[current_node][neighbor]['distance'])

            if neighbor not in visited or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(queue, (priority, neighbor))
                path[neighbor] = current_node

    return None  # No path found

def reconstruct_path(path, goal):
    # Reconstruct the path from the goal node to the start node
    node = goal
    path_list = [node]

    while path[node] is not None:
        node = path[node]
        path_list.append(node)

    return list(reversed(path_list))


# print(AStar("Ramallah", "Rafah"))

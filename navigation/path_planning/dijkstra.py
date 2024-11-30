import heapq

def dijkstra(graph, start, goal):
    queue = [(0, start)]
    distances = {start: 0}
    previous_nodes = {start: None}

    while queue:
        (cost, current_node) = heapq.heappop(queue)
        if current_node == goal:
            break
        for neighbor, weight in graph[current_node]:
            new_cost = cost + weight
            if new_cost < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_cost
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (new_cost, neighbor))

    # Reconstruct the path
    path, current = [], goal
    while current:
        path.insert(0, current)
        current = previous_nodes[current]
    return path, distances[goal]

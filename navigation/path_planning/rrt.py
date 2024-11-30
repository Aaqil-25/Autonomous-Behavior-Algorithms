import random
import math

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

def euclidean_distance(node1, node2):
    return math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

def get_random_node(area):
    return Node(random.uniform(area[0], area[1]), random.uniform(area[2], area[3]))

def rrt(start, goal, area, max_nodes, step_size):
    start_node = Node(*start)
    goal_node = Node(*goal)
    nodes = [start_node]

    for _ in range(max_nodes):
        random_node = get_random_node(area)
        nearest_node = min(nodes, key=lambda n: euclidean_distance(n, random_node))
        theta = math.atan2(random_node.y - nearest_node.y, random_node.x - nearest_node.x)
        new_node = Node(nearest_node.x + step_size * math.cos(theta),
                        nearest_node.y + step_size * math.sin(theta))
        new_node.parent = nearest_node

        if euclidean_distance(new_node, goal_node) <= step_size:
            goal_node.parent = new_node
            nodes.append(goal_node)
            break
        nodes.append(new_node)

    # Reconstruct the path
    path = []
    current = goal_node
    while current is not None:
        path.append((current.x, current.y))
        current = current.parent
    return path[::-1]

# Example usage
if __name__ == "__main__":
    start = (0, 0)
    goal = (10, 10)
    area = (0, 15, 0, 15)
    max_nodes = 1000
    step_size = 1.0
    path = rrt(start, goal, area, max_nodes, step_size)
    print(f"Path: {path}")

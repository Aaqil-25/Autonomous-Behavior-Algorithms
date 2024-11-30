def bug_0(start, goal, obstacles, step_size=0.1):
    current = list(start)
    path = [tuple(current)]

    while tuple(current) != goal:
        direction = [goal[0] - current[0], goal[1] - current[1]]
        norm = (direction[0]**2 + direction[1]**2)**0.5
        step = [step_size * direction[0] / norm, step_size * direction[1] / norm]
        next_position = [current[0] + step[0], current[1] + step[1]]

        if any((obs[0] - next_position[0])**2 + (obs[1] - next_position[1])**2 < step_size**2 for obs in obstacles):
            # Obstacle encountered; follow the boundary (simplified for Bug 0)
            next_position = [current[0] - step[1], current[1] + step[0]]

        current = next_position
        path.append(tuple(current))
        if (goal[0] - current[0])**2 + (goal[1] - current[1])**2 < step_size**2:
            break

    return path

# Example usage
if __name__ == "__main__":
    start = (0, 0)
    goal = (5, 5)
    obstacles = [(2, 2), (3, 3)]
    path = bug_0(start, goal, obstacles)
    print(f"Path: {path}")

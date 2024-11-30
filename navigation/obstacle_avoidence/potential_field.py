
import numpy as np

def attractive_force(current, goal, gain=1.0):
    return gain * (np.array(goal) - np.array(current))

def repulsive_force(current, obstacles, gain=1.0, influence_radius=1.0):
    force = np.zeros(2)
    for obs in obstacles:
        diff = np.array(current) - np.array(obs)
        distance = np.linalg.norm(diff)
        if distance < influence_radius:
            force += gain * (1.0 / distance - 1.0 / influence_radius) / (distance**2) * diff / distance
    return force

def potential_field_navigation(start, goal, obstacles, step_size=0.1, max_steps=100):
    current = np.array(start)
    path = [start]

    for _ in range(max_steps):
        attractive = attractive_force(current, goal)
        repulsive = repulsive_force(current, obstacles)
        total_force = attractive + repulsive
        current += step_size * total_force / np.linalg.norm(total_force)
        path.append(tuple(current))
        if np.linalg.norm(np.array(goal) - current) < 0.1:
            break

    return path

# Example usage
if __name__ == "__main__":
    start = (0, 0)
    goal = (5, 5)
    obstacles = [(2, 2), (3, 3)]
    path = potential_field_navigation(start, goal, obstacles)
    print(f"Path: {path}")

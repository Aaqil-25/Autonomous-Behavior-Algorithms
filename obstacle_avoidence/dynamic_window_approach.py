
import numpy as np

def dynamic_window_approach(state, goal, obstacles, max_speed=1.0, max_turn=1.0, dt=0.1):
    x, y, theta = state
    dx, dtheta = 0.0, 0.0

    best_cost = float('inf')
    best_trajectory = None

    for linear_speed in np.linspace(-max_speed, max_speed, 5):
        for angular_speed in np.linspace(-max_turn, max_turn, 5):
            trajectory = []
            temp_state = [x, y, theta]

            for _ in range(10):  # Simulate 1 second
                temp_state[0] += linear_speed * np.cos(temp_state[2]) * dt
                temp_state[1] += linear_speed * np.sin(temp_state[2]) * dt
                temp_state[2] += angular_speed * dt
                trajectory.append(tuple(temp_state))

                # Check for collisions
                if any(np.linalg.norm(np.array(temp_state[:2]) - np.array(obs)) < 0.5 for obs in obstacles):
                    break

            distance_to_goal = np.linalg.norm(np.array(temp_state[:2]) - np.array(goal))
            if distance_to_goal < best_cost:
                best_cost = distance_to_goal
                best_trajectory = trajectory

    return best_trajectory

# Example usage
if __name__ == "__main__":
    start_state = (0, 0, 0)
    goal = (5, 5)
    obstacles = [(2, 2), (3, 3)]
    trajectory = dynamic_window_approach(start_state, goal, obstacles)
    print(f"Trajectory: {trajectory}")

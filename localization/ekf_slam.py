import numpy as np

class EKFSLAM:
    def __init__(self, initial_state, landmarks, process_noise, measurement_noise):
        self.state = initial_state
        self.P = np.eye(len(initial_state))
        self.landmarks = landmarks
        self.Q = process_noise
        self.R = measurement_noise

    def predict(self, control, motion_model, dt):
        self.state[:3] = motion_model(self.state[:3], control, dt)
        self.P[:3, :3] += self.Q

    def update(self, measurement, measurement_model):
        for i, landmark in enumerate(self.landmarks):
            expected_measurement = measurement_model(self.state, landmark)
            y = measurement[i] - expected_measurement
            H = np.eye(len(self.state))  # Simplified
            S = H @ self.P @ H.T + self.R
            K = self.P @ H.T @ np.linalg.inv(S)
            self.state += K @ y
            self.P = (np.eye(len(self.state)) - K @ H) @ self.P

# Example usage
if __name__ == "__main__":
    initial_state = np.zeros(3)
    landmarks = [np.array([5, 5]), np.array([10, 10])]
    process_noise = np.eye(3) * 0.01
    measurement_noise = np.eye(2) * 0.1

    ekf = EKFSLAM(initial_state, landmarks, process_noise, measurement_noise)
    control = np.array([1, 0.5])
    def motion_model(state, control, dt): return state + control * dt
    def measurement_model(state, landmark): return np.linalg.norm(state[:2] - landmark)
    ekf.predict(control, motion_model, 0.1)
    measurement = [5.1, 10.1]
    ekf.update(measurement, measurement_model)
    print(f"State: {ekf.state}")

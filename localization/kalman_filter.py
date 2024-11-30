import numpy as np

class KalmanFilter:
    def __init__(self, initial_state, state_transition, control_input, observation_model, process_noise, measurement_noise):
        self.state = initial_state
        self.P = np.eye(len(initial_state))
        self.F = state_transition
        self.B = control_input
        self.H = observation_model
        self.Q = process_noise
        self.R = measurement_noise

    def predict(self, control):
        self.state = self.F @ self.state + self.B @ control
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, measurement):
        y = measurement - self.H @ self.state
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.state += K @ y
        self.P = (np.eye(len(self.state)) - K @ self.H) @ self.P

# Example usage
if __name__ == "__main__":
    initial_state = np.array([0, 0])
    state_transition = np.array([[1, 1], [0, 1]])
    control_input = np.array([[0], [1]])
    observation_model = np.eye(2)
    process_noise = np.eye(2) * 0.01
    measurement_noise = np.eye(2) * 0.1

    kf = KalmanFilter(initial_state, state_transition, control_input, observation_model, process_noise, measurement_noise)
    control = np.array([1])
    measurement = np.array([1, 1.5])
    kf.predict(control)
    kf.update(measurement)
    print(f"State: {kf.state}")

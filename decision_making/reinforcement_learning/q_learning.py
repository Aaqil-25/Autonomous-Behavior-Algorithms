import numpy as np

class QLearning:
    def __init__(self, num_states, num_actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = np.zeros((num_states, num_actions))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.q_table.shape[1])
        return np.argmax(self.q_table[state])

    def update(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        target = reward + self.gamma * self.q_table[next_state, best_next_action]
        self.q_table[state, action] += self.alpha * (target - self.q_table[state, action])

# Example usage
if __name__ == "__main__":
    ql = QLearning(num_states=5, num_actions=3)
    ql.update(0, 1, 10, 1)
    print(ql.q_table)

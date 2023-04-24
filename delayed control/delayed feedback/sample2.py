import numpy as np

class ModelBasedAgent:
    def __init__(self, num_states, num_actions, gamma, learning_rate, horizon):
        self.num_states = num_states
        self.num_actions = num_actions
        self.gamma = gamma
        self.learning_rate = learning_rate
        self.horizon = horizon
        self.model = np.zeros((num_states, num_actions, num_states))
        self.rewards = np.zeros((num_states, num_actions))
        self.values = np.zeros(num_states)

    def update_model(self, state, action, reward, next_state):
        self.model[state, action, next_state] += 1
        self.rewards[state, action] += reward

    def plan(self):
        for t in range(self.horizon):
            for state in range(self.num_states):
                for action in range(self.num_actions):
                    expected_reward = np.sum(self.model[state, action] * self.rewards[state, action])
                    expected_value = np.sum(self.model[state, action] * self.values)
                    value_estimate = expected_reward + self.gamma * expected_value
                    self.values[state] += self.learning_rate * (value_estimate - self.values[state])

    def act(self, state):
        expected_values = np.zeros(self.num_actions)
        for action in range(self.num_actions):
            expected_reward = np.sum(self.model[state, action] * self.rewards[state, action])
            expected_value = np.sum(self.model[state, action] * self.values)
            expected_values[action] = expected_reward + self.gamma * expected_value
        return np.argmax(expected_values)

    def update(self, state, action, reward, next_state):
        self.update_model(state, action, reward, next_state)
        self.plan()

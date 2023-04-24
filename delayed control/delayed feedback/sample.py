import torch
import numpy as np

# Define the environment
class Environment:
    def __init__(self, num_states, num_actions, transition_probs, rewards):
        self.num_states = num_states
        self.num_actions = num_actions
        self.transition_probs = transition_probs
        self.rewards = rewards
        self.current_state = 0

    def reset(self):
        self.current_state = 0

    def step(self, action):
        next_state = np.random.choice(self.num_states, p=self.transition_probs[self.current_state][action])
        reward = self.rewards[self.current_state][action][next_state]
        self.current_state = next_state
        return next_state, reward

# Define the model-based agent
class ModelBasedAgent:
    def __init__(self, num_states, num_actions):
        self.num_states = num_states
        self.num_actions = num_actions
        self.transition_probs = torch.zeros(num_states, num_actions, num_states)
        self.rewards = torch.zeros(num_states, num_actions, num_states)
        self.values = torch.zeros(num_states)

    def update_model(self, experience):
        state, action, reward, next_state = experience
        self.transition_probs[state][action][next_state] += 1
        self.rewards[state][action][next_state] += reward

    def plan(self, num_iterations):
        for i in range(num_iterations):
            # Simulate experience using the model
            state = np.random.randint(self.num_states)
            action = np.random.randint(self.num_actions)
            next_state_probs = self.transition_probs[state][action]
            next_state = np.random.choice(self.num_states, p=next_state_probs)
            reward = self.rewards[state][action][next_state]
            simulated_experience = (state, action, reward, next_state)

            # Update the value function using the simulated experience
            gamma = 0.9
            value = reward + gamma * self.values[next_state]
            self.values[state] = value

            # Update the model using the simulated experience
            self.update_model(simulated_experience)

    def act(self, state):
        # Choose the action with the highest expected value
        expected_values = torch.zeros(self.num_actions)
        for action in range(self.num_actions):
            next_state_probs = self.transition_probs[state][action]
            expected_value = torch.sum(next_state_probs * self.values)
            expected_values[action] = expected_value
        return torch.argmax(expected_values)

# Define the training loop
env = Environment(num_states=5, num_actions=2, transition_probs=np.array([[[0.7, 0.3], [0.3, 0.7], [0.3, 0.7], [0.7, 0.3], [0.7, 0.3]],
                                                                          [[0.3, 0.7],

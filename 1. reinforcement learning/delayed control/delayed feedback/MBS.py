import sys
import gym
import torch
import numpy as np

class Model(): # We learn transition kernal & reward function from model learning class
    def __init__(self, n_states, n_actions):
        self.transitions = np.zeros((n_states, n_actions), dtype = np.uint8) # transition probability = deterministic
        self.rewards     = np.zeros((n_states, n_actions))

    def add(self, state, action, next_state, reward):
        self.transitions[state, action] = next_state
        self.rewards[state, action]     = reward

    def sample(self):
        # visit random state
        random_state = np.random.choice(np.where(np.sum(self.transitions, axis = 1) > 0)[0])

        # choice random action in that state
        random_action = np.random.choice(np.where(self.transitions[random_state] >0)[0])

        return random_state, random_action

    def step(self, state, action):
        next_state = self.transitions[state][action]
        reward     = self.rewards[state][action]
        return next_state, reward

class MBS():
    def __init__(self):
        self.env   = gym.make('Taxi-v3')
        self.q     = np.zeros((self.env.observation_space.n, self.env.action_space.n))
        self.model = Model(self.env.observation_space.n, self.env.action_space.n)

        self.n     = 5
        self.alpha = 0.01
        self.gamma = 0.95
        self.max_steps = 100

    def learn(self):
        state = self.env.reset()[0]
        total_reward = 0

        # Loop forever
        for step in range(self.max_steps):
            if np.random.uniform() < 0.1:
                action = self.env.action_space.sample()
            else:
                action = np.argmax(self.q[state])

            next_state, reward, done, _, _ = self.env.step(action)
            self.q[state, action] = self.q[state, action] + self.alpha*(reward + self.gamma*np.max(self.q[next_state]) - self.q[state, action])

            self.model.add(state, action, next_state, reward)
            self.planning()

            total_reward += reward
            state = next_state

            if done:
                s = self.env.reset()

        return total_reward, self.q

    def planning(self): # make optimal value function / optimal policy
        for i in range(self.n):
            state, action         = self.model.sample()
            next_state, reward    = self.model.step(state, action)
            self.q[state, action] = self.q[state, action] + self.alpha*(reward + self.gamma*np.max(self.q[next_state]) - self.q[state, action])


simple_model = MBS()

Q = 0
beta = 0.001
for i in range(5000):
    total_reward, Q = simple_model.learn()

    print(np.sum(Q))



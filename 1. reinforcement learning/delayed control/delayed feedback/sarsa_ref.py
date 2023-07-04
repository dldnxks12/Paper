
import gymnasium as gym
import sys
import numpy as np
import random
from time import sleep



def behavior_policy(random_policy, state, epsilon):
    if random.random() < epsilon:
        action = env.action_space.sample()
    else:
        action = np.argmax(random_policy[state, :])

    return action


def Sarsa(env, random_policy,  Y, epsilon, n_epsiodes):
    Q = np.zeros([nS, nA])
    for e in range(n_epsiodes):
        state = env.reset()[0]  # Initial State

        gamma = 0.9
        alpha = 0.1

        total_reward = 0
        done = False
        truncated = False

        while True:
            if random.random() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state, :])

            next_state, reward, done, done2, _ = env.step(action)
            total_reward += reward
            next_action = np.argmax(Q[next_state, :])

            Q[state][action] = ((1-alpha) * Q[state][action]) + (alpha*(reward + gamma * Q[next_state][next_action]))

            state = next_state

            if done == True or done2 == True:
                break

        Y.append(total_reward)
        print(f"Episode : {e} || total_reward : {total_reward}")

    Y = np.array(Y)
    np.save('./Sarsa_ref', Y)
    return Q

Y = []

env = gym.make('Taxi-v3').env
env = gym.wrappers.TimeLimit(env, max_episode_steps = 30)

nS = env.observation_space.n
nA = env.action_space.n
random_policy = np.ones([nS, nA]) / nA

Q = Sarsa(env, random_policy, Y , epsilon = 0.0, n_epsiodes = 5000)

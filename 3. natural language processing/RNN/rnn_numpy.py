import numpy as np

timestep = 10    # 문장 길이
input_dim = 4    # 입력 단어의 차원
hidden_units = 8

inputs = np.random.random((timestep, input_dim)) # 10 x 4
hidden_state_t = np.zeros((hidden_units, ))  # [0. 0. 0. 0. 0. 0. 0. 0.] (8,)

Wx = np.random.random((hidden_units, input_dim))
Wh = np.random.random((hidden_units, hidden_units))
b  = np.random.random((hidden_units, ))

total_hidden_states = []

for input_time_step in inputs: # 10개의 time step, 4 차원 입력

    output_t = np.tanh(np.dot(Wx, input_time_step) + np.dot(Wh, hidden_state_t) + b)

    # 각 time step 마다의 hidden unit 값
    # i.e h1, h2, h3, ... , ht
    total_hidden_states.append(list(output_t))
    hidden_state_t = output_t # 다음으로 transfer


total_hidden_states = np.stack(total_hidden_states, axis = 0)
print(total_hidden_states)

# Remember to adjust your student ID in meta.xml
import numpy as np
import pickle
import random
import gym
import os

def load_data():
    if os.path.exists("q_table.pkl"):
        with open("q_table.pkl", "rb") as f:
            q_table = pickle.load(f)
    else: 
        q_table = {}
    
    return q_table


def get_action(obs):
    
    # TODO: Train your own agent
    # HINT: If you're using a Q-table, consider designing a custom key based on `obs` to store useful information.
    # NOTE: Keep in mind that your Q-table may not cover all possible states in the testing environment.
    #       To prevent crashes, implement a fallback strategy for missing keys. 
    #       Otherwise, even if your agent performs well in training, it may fail during testing.


    # NOTE 
    # obs = (taxi_row, taxi_col, self.stations[0][0],self.stations[0][1] ,self.stations[1][0],self.stations[1][1],self.stations[2][0],self.stations[2][1],self.stations[3][0],self.stations[3][1],obstacle_north, obstacle_south, obstacle_east, obstacle_west, passenger_look, destination_look)
    # obs = (taxi_pos, R_pos, G_pos, y_pos, B_pos, obstacle_north, obstacle_south, obstacle_east, obstacle_west, passenger_look, destination_look) 
    q_table = load_data()
    action_space = [0, 1, 2, 3, 4, 5]
    #state = obs

    taxi_pos = (obs[0], obs[1])

    # obstacle_north, obstacle_south, obstacle_east, obstacle_west = obs[10:14]
    passenger_look, drop_look = obs[14], obs[15]

    # Reconstruct `passenger_in_taxi` as done in training
    passenger_in_taxi = getattr(get_action, "passenger_in_taxi", False)
    station_positions = [(obs[i], obs[i + 1]) for i in range(2, 10, 2)]

    previous_taxi_pos = getattr(get_action, "previous_taxi_pos", None)

    if previous_taxi_pos in station_positions and taxi_pos != previous_taxi_pos and not passenger_in_taxi:
        passenger_in_taxi = True  # Infer that the passenger was picked up
        

    get_action.previous_taxi_pos = taxi_pos
    get_action.passenger_in_taxi = passenger_in_taxi

    # Use the same state representation as training
    state = obs[0:2] + obs[10:16] + (passenger_in_taxi,)
        
    if state not in q_table:
        action = np.random.choice(action_space, p=[0.25, 0.25, 0.25, 0.25, 0, 0])
    epsilon = 0.05
    if np.random.rand() < epsilon:
        action = np.random.choice(action_space)  # Small chance of exploring
    else:
        max_q_value = np.max(q_table[state])
        best_actions = [i for i, q in enumerate(q_table[state]) if q == max_q_value]
        action =  np.random.choice(best_actions)
    
    return action

    # q_values = q_table[state]
    # probabilities = np.exp(q_values) / np.sum(np.exp(q_values))  # Softmax
    # action = np.random.choice(action_space, p=probabilities)

    # q_values = q_table[state]
    # exp_q_values = np.exp(q_values / 0.5)
    # prob_distribution = exp_q_values / np.sum(exp_q_values)
    # return np.random.choice(len(q_values), p=prob_distribution)
    # max_q_value = np.max(q_table[state])
    # best_actions = [i for i, q in enumerate(q_table[state]) if q == max_q_value]

    # # Randomly choose one of the best actions
    # action = np.random.choice(best_actions)

    # return action
    # You can submit this random agent to evaluate the performance of a purely random strategy.


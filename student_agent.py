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
    q_table, _ = load_data()
    state = obs

    # penalize for hitting obstacles    
    if state not in q_table:
        q_table[state] = np.zeros(6, dtype=np.float32)

    max_q_value = np.max(q_table[state])
    best_actions = [i for i, q in enumerate(q_table[state]) if q == max_q_value]

    # Randomly choose one of the best actions
    action = np.random.choice(best_actions)


    return action
    # You can submit this random agent to evaluate the performance of a purely random strategy.


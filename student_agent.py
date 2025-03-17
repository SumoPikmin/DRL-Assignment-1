# Remember to adjust your student ID in meta.xml
import numpy as np
import pickle
import random
import gym

def get_action(obs):
    
    # TODO: Train your own agent
    # HINT: If you're using a Q-table, consider designing a custom key based on `obs` to store useful information.
    # NOTE: Keep in mind that your Q-table may not cover all possible states in the testing environment.
    #       To prevent crashes, implement a fallback strategy for missing keys. 
    #       Otherwise, even if your agent performs well in training, it may fail during testing.

    # TODO state representation agent pos(x,y), pickup pos (x,y), dropoff(x,y), , passenger_picked_up: (0,1 if passenger is picked up), goal(x, y) maybe obstacle location or just penalize for hitting obstacles 

    # TODO reward shaping, only pickup if no passenger and on the correct field, only dropoff if passenger and on the correct field
    # after correct pickup, move to destination
    # penalize for hitting obstacles    
    reward_shaping = True
    picked_bonus_claimed = False

    # if reward_shaping:
    #     shaped_reward = 0
    #     if not picked_up_now and picked_up_before:
    #         shaped_reward -= 0.3
    #     if picked_up_now and not picked_up_before and not pickup_bonus_claimed:
    #         shaped_reward += 0.5
    #     # TODO how to decentivize running in obstacles
    #     goal_x, goal_y = state[7], state[8]
    #     agent_pos_x, agent_pos_y = state[0], state[1]
    #     new_agent_pos_x, new_agent_pos_y = next_state[0], next_state[1]
    #     d_goal_before = abs(agent_pos_x - goal_x) + abs(agent_pos_y - goal_y)
    #     d_goal_after  = abs(next_state[0] - goal_x) + abs(next_state[1] - goal_y)

    #     if picked_up_now and (d_goal_after < d_goal_before):
    #         shaped_reward += 0.08
    #     elif picked_up_now and (d_goal_after > d_goal_before):
    #         shaped_reward -= 0.04


    return random.choice([0, 1, 2, 3, 4, 5]) # Choose a random action
    # You can submit this random agent to evaluate the performance of a purely random strategy.


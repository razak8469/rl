import gym

import numpy as np
import copy

import check_test
import math

env = gym.make("FrozenLake-v0")
# print(env.P)

def policy_evaluation(env, policy, gamma=1, theta=1e-8):
    V = np.zeros(env.nS)

    ## TODO: complete the function
    i = 0
    while True:
        i += 1
        delta = 0
        for i_s, v in enumerate(V):
            v_new = 0.0
            for i_a, p_a_s in enumerate(policy[i_s]):
                for p, i_ns, r, _ in env.P[i_s][i_a]:
                    v_new += p_a_s*p*(r + gamma*V[i_ns])
            delta = max(delta, abs(v - v_new))
            V[i_s] = v_new
        if delta < theta:
            break
    print("Evaluated in {} iterations".format(i))
    return

# policy_evaluation(env, 1)

policy = random_policy = np.ones([env.nS, env.nA]) / env.nA
print(policy)

V = policy_evaluation(env, random_policy)
print(V)
env.close()

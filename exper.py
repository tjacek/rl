import q_learning,baby
import numpy as np
import matplotlib.pyplot as plt

def exper(n_epochs=100,window=100):
    envir=baby.CryingBaby()
    q_learn=q_learning.QLearn()
    mean_rewards=[]
    for i in range(n_epochs):
        q_learn(envir,window)
        envir.reset()
        rewards_i=q_learn.no_learning(envir,window)
        mean_rewards.append(np.mean(rewards_i))
    plt.plot(mean_rewards)
    plt.ylabel('rewards')
    plt.show()

exper()
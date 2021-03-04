import q_learning,baby
import numpy as np
import matplotlib.pyplot as plt

def exper(n_epochs=100,window=30):
    envir=baby.CryingBaby()
    q_learn=q_learning.QLearn()
    rewards=q_learn(envir,n_epochs)
    rewards=np.array(rewards)
    average=np.convolve(rewards,np.ones(window), 'valid') / window
    plt.plot(average)
    plt.ylabel('rewards')
    plt.show()

exper()
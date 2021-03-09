import q_learning,envir.baby,envir.bandit
import numpy as np
import matplotlib.pyplot as plt

def exper(n_epochs=1000,window=10):
    exper_envir=envir.bandit.make_binomial_bandit()
#    exper_envir=envir.baby.CryingBaby()
    q_learn=q_learning.make_simulation()#QLearn()
    rewards=q_learn(exper_envir,n_epochs)
    mean_rewards=[ np.mean(rewards[i*window:(i+1)*window]) 
                    for i in range(int(n_epochs/window))] 
    plt.plot(mean_rewards)
    plt.ylabel('rewards')
    plt.show()

exper()

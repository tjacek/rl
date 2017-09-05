import envir 
import q_learning
import numpy as np

class Experiment(object):
    def __init__(self,envir,alg,epsi=0.1):
        self.envir=envir
        self.alg=alg
        self.epsi=epsi

    def next_step(self):
        state_i=self.envir.get_current_state()
        action_i=self.select_action(state_i)
        reward_i=self.envir.next_step(action_i)
        self.alg.update(state_i,action_i,reward_i)
        return (action_i,reward_i)

    def select_action(self,state_i):
    	p=np.random.uniform()
        if(p>self.epsi):
            return self.alg.q.best_action(state_i)
        else:
        	actions=self.envir.get_actions()
        	return np.random.choice(actions)

bandit=envir.make_binomial_bandit()
q=q_learning.make_qfactor_lookup(bandit)
alg=q_learning.QLearningAlg(q,0.9,0.5)
exper=Experiment(bandit,alg)
for i in range(5000):
    print(exper.next_step())
print(bandit)
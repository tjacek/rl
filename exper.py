import envir 
import q_learning

class Experiment(object):
    def __init__(self,envir,alg):
        self.envir=envir
        self.alg=alg

    def next_step(self):
        state_i=self.envir.get_current_state()
        action_i=self.alg.q.best_action(state_i)
        reward_i=self.envir.next_step(action_i)
        self.alg.update(state_i,action_i,reward_i)
        return (action_i,reward_i)

bandit=envir.make_binomial_bandit()
q=q_learning.make_qfactor_lookup(bandit)
alg=q_learning.QLearningAlg(q,0.9,0.5)
exper=Experiment(bandit,alg)
for i in range(50):
    print(exper.next_step())	
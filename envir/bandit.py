import numpy as np 
import envir

class MultiArmBandit(envir.Enviroment):
    def __init__(self,dists):
        super(MultiArmBandit, self).__init__(state=0)
        self.dists=dists

    def __str__(self):
        bandit_txt=''
        for dist_i in self.dists:
            bandit_txt+=str(dist_i)+'\n'    
        return bandit_txt   

    def get_actions(self):
        return range(len(self.dists))

    def get_states(self):
        return [self.state] 
     
    def next_step(self,action_i):
        if(not envir.is_int(action_i)):
            raise envir.NonIntAction(action_i)
        reward=float(self.dists[action_i]())
        return reward

def make_binomial_bandit(n=10):
    params=[np.random.uniform()
                for i in range(n)]
    dists=[ BinomialDist(param_i,n) 
                for param_i in params]
    return MultiArmBandit(dists)
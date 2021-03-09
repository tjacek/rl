import numpy as np 
import envir

class MultiArmBandit(object):
    def __init__(self,dists):
        self.last_action=0
        self.dists=dists

    def __str__(self):
        return ",".join([ str(dist_i) for dist_i in self.dists] )  

    def get_actions(self):
        return len(self.dists)#range(len(self.dists))

    def get_states(self):
        return 1#[0] 
    
    def observe(self):
        return 0

    def reset(self):
        return None

    def act(self,action_i):
        print(action_i)
        return self.dists[action_i]()

class BinomialDist(object):
    def __init__(self,p=0.5,n=10):
        self.p=p
        self.n=n

    def __call__(self):        
        return np.random.binomial(n=self.n,p=self.p)

    def __str__(self):
        return 'p:'+str(self.p)

def make_binomial_bandit(n=10):
    params=[np.random.uniform()
                for i in range(n)]
    dists=[ BinomialDist(param_i,n) 
                for param_i in params]
    return MultiArmBandit(dists)
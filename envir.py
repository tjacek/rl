import numpy as np 

class MultiArmBandit(object):
    def __init__(self,dists):
        self.dists=dists

    def __len__(self):
        return len(self.dists)

    def get_actions(self):
        return range(len(self))
     
    def next_step(self,action_i):
        if(type(action_i)==int):
            return Exception('Action must be Integer')
        return float(self.dists[i]())
		
class BinomialDist(object):
    def __init__(self,p=0.5,n=10):
        self.p=p
        self.n=n

    def __call__(self):        
        return np.random.binomial(n=self.n,p=self.p)

def make_binomial_bandit(n=10):
    params=[np.random.uniform()
                for i in range(n)]
    dists=[ BinomialDist(param_i,n) 
                for param_i in params]
    return dists
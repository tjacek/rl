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
        if(type(action_i)==int):
            return Exception('Action must be Integer')
        reward=float(self.dists[action_i]())
        return reward

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
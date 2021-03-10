import numpy as np 
import envir.baby

class Simulation(object):
    def __init__(self,policy,update):
        self.policy=policy
        self.update=update
        self.model=None

    def __call__(self,s_envir,n_epochs=100):
        if(self.model is None):
            self.model=np.random.rand(s_envir.get_states(),s_envir.get_actions())
        rewards=[]
        old_state=s_envir.observe()
        for i in range(n_epochs):
            act_i= self.policy(old_state,self.model)
            r_i=s_envir.act(act_i)
            next_state=s_envir.observe()
            self.update(old_state,next_state,act_i,r_i,self.model)
            old_state=next_state
            rewards.append(r_i)
        return np.array(rewards)

class QLearn(object):
    def __init__(self,alpha=0.05,gamma=0.9):
        self.alpha=alpha
        self.gamma=gamma

    def __call__(self,old_state,next_state,act_i, r_i,q):
        future=self.gamma*max(q[next_state,:])
        q[old_state,act_i]=(1-self.alpha)*q[old_state,act_i]+self.alpha*(r_i+future)
        
class Sarsa(object):
    def __init__(self,alpha=0.05,gamma=0.9):
        self.alpha=alpha
        self.gamma=gamma
        
    def __call__(self,old_state,next_state,act_i, r_i,q):
        future=self.gamma*Q[next_state,act_i]
        q[obs_i,act_i]=(1-self.alpha)*q[obs_i,act_i]+self.alpha*(r_i+future)

class EpsilonGreedy(object):
    def __init__(self,eps,discount=0.9):
        self.eps=eps
        self.discount=discount

    def __call__(self,state_i,q):
        if(np.random.uniform()>self.eps):
            return best_action(state_i,q)
        self.eps*=self.discount
        return np.random.randint(0,q.shape[1])

class Boltzmann(object):
    def __init__(self, T=0.6):
        self.T=T
    
    def __call__(self,state_i,q):
        dist=np.exp(q[state_i]/self.T)
        dist=dist/np.sum(dist)
        a=range(q.shape[1])
        return np.random.choice(a,None,True,dist)

def best_action(state_i,q):
    return np.argmax(q[state_i])

def make_simulation():
    update=QLearn()
    policy=EpsilonGreedy(0.9)
    return Simulation(policy,update)

if __name__ == "__main__":
    exper_envir=envir.baby.CryingBaby()
    q_learn=Sarsa()
    print(q_learn(exper_envir))
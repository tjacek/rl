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
        obs_i=s_envir.observe()
        for i in range(n_epochs):
            act_i= self.policy(obs_i,self.model)
            r_i=s_envir.act(act_i)
            obs_i=s_envir.observe()
            self.update(obs_i,act_i, r_i,self.model)
            rewards.append(r_i)
        return np.array(rewards)

class QLearn(object):
    def __init__(self,alpha=0.05,gamma=0.9):
        self.alpha=alpha
        self.gamma=gamma

    def __call__(self,obs_i,act_i, r_i,q):
        future=self.gamma*best_action(obs_i,q)
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

def best_action(state_i,q):
    return np.argmax(q[state_i])

def make_simulation():
    update=QLearn()
    policy=EpsilonGreedy(0.9)
    return Simulation(policy,update)

if __name__ == "__main__":
    exper_envir=envir.baby.CryingBaby()
    q_learn=QLearn()
    print(q_learn(exper_envir))
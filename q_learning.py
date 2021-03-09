import numpy as np 
import envir.baby

class QLearn(object):
    def __init__(self,alpha=0.05,gamma=0.9,eps=0.1):
        self.alpha=alpha
        self.gamma=gamma
        self.policy=EpsilonGreedy(eps)
        self.q=None

    def __call__(self,exper_envir,n_epochs=100):
        if(self.q is None):
            self.q=np.random.rand(exper_envir.get_states(),exper_envir.get_actions() )
        rewards=[]
        obs_i=exper_envir.observe()
        for i in range(n_epochs):
            act_i= self.policy(obs_i,self.q)
            r_i=exper_envir.act(act_i)
            obs_i=exper_envir.observe()
            future=self.gamma*best_action(obs_i,self.q)
            self.q[obs_i,act_i]=(1-self.alpha)*self.q[obs_i,act_i]+self.alpha*(r_i+future)
            rewards.append(r_i)
        return rewards

    def no_learning(self,exper_envir,n_epochs):
        rewards=[]
        for i in range(n_epochs):
            obs_i=exper_envir.observe()
            action_i=best_action(obs_i,self.q)
            rewards.append(exper_envir.act(action_i))
        return rewards
        
class EpsilonGreedy(object):
    def __init__(self,eps):
        self.eps=eps

    def __call__(self,state_i,q):
        if(np.random.uniform()>self.eps):
            return best_action(state_i,q)
        return np.random.randint(0,q.shape[1])

def best_action(state_i,q):
    return np.argmax(q[state_i])

if __name__ == "__main__":
    exper_envir=envir.baby.CryingBaby()
    q_learn=QLearn()
    print(q_learn(exper_envir))
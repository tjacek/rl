import numpy as np 
import baby

class QLearn(object):
    def __init__(self,alpha=0.5,gamma=0.9,eps=0.1):
        self.alpha=alpha
        self.gamma=gamma
        self.eps=eps
        self.q=None

    def __call__(self,envir,n_epochs=100):
        states=envir.get_states()
        actions=envir.get_actions()
        if(self.q is None):
            self.q=np.random.rand(len(states),len(actions))
        rewards=[]
        obs_i=envir.observe()
        for i in range(n_epochs):
            x=obs_i.value
            y=self.next_action(obs_i)
            action_i=actions[y]
            r_i=envir.act(action_i)
            obs_i=envir.observe()
            future=self.gamma*self.best_action(obs_i)  #np.argmax(q[obs_i.value])
            self.q[x,y]=(1-self.alpha)*self.q[x,y]+self.alpha*(r_i+future)
            rewards.append(r_i)
        return rewards

    def next_action(self,state_i):
        if(np.random.uniform()>self.eps):
            return self.best_action(state_i)
        return np.random.randint(0,self.q.shape[1])

    def best_action(self,state_i):
        return np.argmax(self.q[state_i.value])

envir=baby.CryingBaby()
q_learn=QLearn()
print(q_learn(envir))
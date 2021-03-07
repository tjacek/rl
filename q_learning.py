import numpy as np 
import envir.baby

class QLearn(object):
    def __init__(self,alpha=0.05,gamma=0.9,eps=0.1):
        self.alpha=alpha
        self.gamma=gamma
        self.eps=eps
        self.q=None

    def __call__(self,exper_envir,n_epochs=100):
        states=exper_envir.get_states()
        actions=exper_envir.get_actions()
        if(self.q is None):
            self.q=np.random.rand(len(states),len(actions))
        rewards=[]
        obs_i=exper_envir.observe()
        for i in range(n_epochs):
            x=obs_i#.value
            y=self.next_action(obs_i)
            action_i=actions[y]
            r_i=exper_envir.act(action_i)
            obs_i=exper_envir.observe()
            future=self.gamma*self.best_action(obs_i)  #np.argmax(q[obs_i.value])
            self.q[x,y]=(1-self.alpha)*self.q[x,y]+self.alpha*(r_i+future)
            rewards.append(r_i)
        return rewards

    def no_learning(self,exper_envir,n_epochs):
        rewards=[]
        for i in range(n_epochs):
            obs_i=exper_envir.observe()
            action_i=self.best_action(obs_i)
            rewards.append(exper_envir.act(action_i))
        return rewards

    def next_action(self,state_i):
        if(np.random.uniform()>self.eps):
            return self.best_action(state_i)
        return np.random.randint(0,self.q.shape[1])

    def best_action(self,state_i):
        return np.argmax(self.q[state_i])#.value])

if __name__ == "__main__":
    exper_envir=envir.baby.CryingBaby()
    q_learn=QLearn()
    print(q_learn(exper_envir))

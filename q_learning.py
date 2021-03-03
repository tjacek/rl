import numpy as np 
import baby

def q_learn(envir,n_epochs=100,alpha=0.5,gamma=0.9):
    states=envir.get_states()
    actions=envir.get_actions()
    q=np.random.rand(len(states),len(actions))
    rewards=[]
    obs_i=envir.observe()
    for i in range(n_epochs):
        x=obs_i.value
        y=np.argmax(q[x])
        action_i=actions[y]
        r_i=envir.act(action_i)
        obs_i=envir.observe()
        future=gamma*np.argmax(q[obs_i.value])
        q[x,y]=(1-alpha)*q[x,y]+alpha*(r_i+future)
        rewards.append(r_i)
    return rewards

envir=baby.CryingBaby()
print(q_learn(envir))
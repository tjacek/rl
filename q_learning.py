import numpy as np 

class QLearningAlg(object):
    def __init__(self,q,alpha,gamma):
        self.q=q
        self.alpha=alpha 
        self.gamma=gamma
        
    def update(self,state_i,action_i,r_i):
        old_value=self.q(state_i,action_i)
        new_value=old_value+ self.alpha*(r_i + self.gamma*self.q.max(state_i) - old_value)
        self.q(state_i,action_i,new_value) 

class QFactorLookup(object):
    def __init__(self,q):
        self.q=q

    def __call__(self,state_i,action_i,value=None):
        if(value!=None):
            self.q[state_i][action_i]=value
        return self.q[state_i][action_i]

    def max(self,state_i):
        return max(self.q[state_i])

    def best_action(self,state_i):
        expected_values=np.array(self.q[state_i])
        return np.argmax(expected_values)

def make_qfactor_lookup(envir):
    actions=envir.get_actions()
    states=envir.get_states()
    init_values={ state_i:{action_i:0.0 
                            for action_i in actions}
                                for state_i in states}
    return QFactorLookup(init_values)
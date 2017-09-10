import envir
import numpy as np
import utils

class MarkovDP(object):
    def __init__(self, trans,rewards):
        self.trans = trans
        self.rewards=rewards
    
    def __str__(self):
        return str(self.trans)

    def get_actions(self):
        return range(self.trans.shape[2])

    def get_states(self):
        return range(self.trans.shape[0])  

    def next_step(self,action_i):
        if(not envir.is_int(action_i)):
            raise envir.NonIntAction(action_i)
        old_state= self.get_current_state()
        dist_i=self.trans[old_state]
        new_state=np.random.choice(self.get_states(), None, p=dist_i)
        return self.rewards[old_state][new_state]

class MarkovChain(envir.Enviroment):
    def __init__(self,trans,start_state=0):
        super(MarkovChain, self).__init__(state=start_state)	
        self.trans=trans
    
    def __str__(self):
        return str(self.trans)

    def get_actions(self):
        return range(self.trans.shape[0])

    def get_states(self):
        return range(self.trans.shape[0])

    def next_step(self,action_i):
        if(not envir.is_int(action_i)):
            raise envir.NonIntAction(action_i)
        old_state= self.get_current_state()
        dist_i=self.trans[old_state]
        new_state=np.random.choice(self.get_states(), None, p=dist_i)
        print(new_state)
        self.state=new_state
        return float(new_state==action_i)

def make_markov_decision(n_states,n_actions):
    trans=[utils.make_stoch_matrix(n_states)
            for i in range(n_actions)]
    trans=np.array(trans)
    rewards=np.random.rand(n_states,n_states)
    return MarkovDP(trans,rewards)

def make_markov_chain(n):
    return MarkovChain(utils.make_stoch_matrix(n))
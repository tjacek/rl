import envir
import numpy as np
import utils

class MarkovDP(envir.Enviroment):
    def __init__(self, trans,rewards):
        super(MarkovDP, self).__init__(state=0)
        self.trans = trans
        self.rewards=rewards
    
    def __str__(self):
        return str(self.trans)

    def get_actions(self):
        return range(self.trans.shape[0])

    def get_states(self):
        return range(self.trans.shape[2])  

    def next_step(self,action_i):
        if(not envir.is_int(action_i)):
            raise envir.NonIntAction(action_i)
        old_state= self.get_current_state()
        dist_i=list(self.trans[action_i][old_state])
        new_state=np.random.choice(self.get_states(), None, p=dist_i)
        return self.rewards[old_state][new_state]

class MarkovChain(object):
    def __init__(self,trans,start_state=0):
        self.trans=trans
        self.state=state

    def __str__(self):
        return str(self.trans)

    def __len__(self):
        return self.trans.shape[0]
    
    def gen_seq(self,n):
        return [ self.next_step() 
                    for i in range(n)]

    def next_step(self):
        old_state= self.state
        dist_i=self.trans[old_state]
        new_state=np.random.choice(self.get_states(), None, p=dist_i)
        self.state=new_state
        return self.state

def make_markov_decision(n_states,n_actions):
    trans=[utils.make_stoch_matrix(n_states)
            for i in range(n_actions)]
    trans=np.array(trans)
    rewards=np.random.rand(n_states,n_states)
    return MarkovDP(trans,rewards)

def make_markov_chain(n):
    return MarkovChain(utils.make_stoch_matrix(n))
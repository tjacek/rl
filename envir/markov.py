import envir
import numpy as np

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
        if(type(action_i)==int):
            return Exception('Action must be Integer')
        old_state= self.get_current_state()
        dist_i=self.trans[old_state]
        new_state=np.random.choice(self.get_states(), None, p=dist_i)
        print(new_state)
        self.state=new_state
        return float(new_state==action_i)

def make_markov_chain(n):
    dists=[ get_distribution(n)
             for i in range(n)]
    trans=np.array(dists)
    return MarkovChain(trans)
class Game(object):
    def __init__(self,payoff,strategy_a,strategy_b):
        self.payoff=payoff	
        self.strategy_a=strategy_a
        self.strategy_b=strategy_b

    def play(self,n_iters):
    	for iter_i in range(n_iters):
    		a_i=self.strategy_a.get_action(iter_i)
            b_i=self.strategy_b.get_action(iter_i)
            self.strategy_a.update(b_i)
            self.strategy_b.update(a_i)


class Tic(object):
    def __init__(self):
        self.prev=None

    def get_action(self,iter_i):
    	if(iter_i==0):
    		return 0
        return self.prev

    def update(self,action_i):
        return action_i	
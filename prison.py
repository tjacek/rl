import numpy as np

class Game(object):
    def __init__(self,payoff=None):
        if(payoff is None):
        	payoff=np.array([[-1,0],
        		             [-3,-2]])
        self.payoff=payoff	

    def n_actions(self):
        return self.payoff.shape[0]
    
    def play(self,strategy_a,strategy_b,n_iters):
    	payoff_a,payoff_b=0.0,0.0
    	for iter_i in range(n_iters):
    		a_i=strategy_a.get_action(iter_i)
            b_i=strategy_b.get_action(iter_i)
            strategy_a.update(b_i)
            strategy_b.update(a_i)
            payoff_a+=self.payoff[a_i][b_i]
            payoff_b+=self.payoff[b_i][a_i]
        return payoff_a,payoff_b

class Tournament(object):
    def __init__(self,game,strategies):
        self.game=game
        self.strategies=[ strategy_i(self.gmae)
                for strategy_i in strategies]

    def __call__(self,n_iters):
        score_dict={}
        n_players=len(self.strategies)
        for i in range(n_players):
            for j in range(i,n_players):
                strategy_i=self.strategies[i]
                strategy_j=self.strategies[j]
                payoff_a,payoff_b=self.game.play(strategy_a=strategy_i,
                                                 strategy_b=strategy_j,
                                                 n_iters=n_iters)
                score_dict[str(strategy_i)]=payoff_a
                score_dict[str(strategy_j)]=payoff_b
        return score_dict

class Strategy(object):
    def __init__(self,game):
        pass

    def get_action(self,iter_i):
        return 0

    def update(self,action_i):
        pass

class Tic(Strategy):
    def __init__(self,game):
        self.prev=None

    def get_action(self,iter_i):
    	if(iter_i==0):
    		return 0
        return self.prev

    def update(self,action_i):
        self.prev=action_i	

    def __str__(self):
        return "Tic"

class UnCoperation(Strategy):
    def get_action(self,iter_i):
        return 0

    def __str__(self):
        return "Cu"

class UnDefection(Strategy):
    def get_action(self,iter_i):
        return 1

    def __str__(self):
        return "Du"

class Random(Strategy):
    def __init__(self,game):
        self.n_actions=game.n_actions()
    
    def get_action(self,iter_i):
        return np.random.randint(self.n_actions)

    def __str__(self):
        return "Random"
import numpy as np

class Game(object):
    def __init__(self,payoff_a=None,payoff_b=None):
        self.payoff_a=payoff_a	
        self.payoff_b=payoff_b

    def n_actions(self):
        return self.payoff_a.shape[0]

    def zero_sum(self):
        payoff_sum=self.payoff_a+self.payoff_b
        value=payoff_sum[0][0]
        return np.all(payoff_sum == value)

    def play(self,strategy_a,strategy_b,n_iters):
        value_a,value_b=0.0,0.0
        for iter_i in range(n_iters):
            a_i=strategy_a.get_action(iter_i)
            b_i=strategy_b.get_action(iter_i)
            strategy_a.update(b_i)
            strategy_b.update(a_i)
            value_a+=self.payoff_a[a_i][b_i]
            value_b+=self.payoff_b[b_i][a_i]
        return value_a/n_iters,value_b/n_iters

def prisoner_dillema():    
    payoff_a=np.array([[4,5],
                       [1,2]])
    payoff_b=np.array([[4,1],
                       [5,2]])
    return Game(payoff_a=payoff_a,
                payoff_b=payoff_b)

def battle_of_sexes():
    payoff_a=np.array([[5,1],
                       [2,6]])
    payoff_b=np.array([[6,1],
                       [2,5]])
    return Game(payoff_a=payoff_a,
                payoff_b=payoff_b)

class Tournament(object):
    def __init__(self,game=None,strategies=None):
        if(game is None):
            game=Game()        
        if(strategies is None):
            strategies=[Tic,UnCoperation,UnDefection,Random]
        self.game=game
        self.strategies=[ strategy_i(self.game)
                for strategy_i in strategies]

    def __call__(self,n_iters):
        score_dict,pairwise={},[]
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
                pairwise.append((str(strategy_i),payoff_a,
                                 str(strategy_j),payoff_b))
        return score_dict,pairwise

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

if __name__ == "__main__":
   game= battle_of_sexes()
   tour=Tournament(game)
   result_dict,pairwise=tour(10)
   print(pairwise)
   print(result_dict)
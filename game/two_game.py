import numpy as np
from scipy.optimize import linprog
import core

class TwoPlayer(object):
    def __init__(self,payoff=None):
        self.payoff=payoff

    def n_actions(self):
        return self.payoff.shape[0]

    def play(self,strategy_a,strategy_b,n_iters=1):
        value_a,value_b=0.0,0.0
        for iter_i in range(n_iters):
            a_i=strategy_a.get_action(iter_i)
            b_i=strategy_b.get_action(iter_i)
            strategy_a.update(b_i)
            strategy_b.update(a_i)
            value_a+=self.payoff_a[a_i][b_i]
            value_b+=self.payoff_b[b_i][a_i]
        return value_a/n_iters,value_b/n_iters

class MixedStrategy(core.Strategy):
    def __init__(self,p):
        self.p=p

    def get_action(self,iter_i):
        return np.random.choice(a=len(self.p), 
                                p=self.p)

    def update(self,action_i):
        pass
    
    def __str__(self):
        return "Mixed"

    def find_best(self):

class NashEquilib(object):
    def __init__(self,q,p):
        self.p=p
        self.q=q

def find_equil(game,q):
    n_actions=game.n_actions()
    A_ub= q @ game.payoff
    result=linprog(c=p, 
                   A_ub= q @ A, 
                   b_ub=None, 
                   A_eq=numpy.identity(n_actions), 
                   b_eq=None, 
                   bounds=(0.0,1.0), 
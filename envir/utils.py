import numpy as np 

class BinomialDist(object):
    def __init__(self,p=0.5,n=10):
        self.p=p
        self.n=n

    def __call__(self):        
        return np.random.binomial(n=self.n,p=self.p)

    def __str__(self):
        return 'p:'+str(self.p)

def get_distribution(n):
    dist=np.random.rand(n)
    c=sum(dist)
    dist/=c
    return dist
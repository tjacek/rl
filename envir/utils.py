import numpy as np 



def make_stoch_matrix(n):
    dists=[ get_distribution(n)
             for i in range(n)]
    return np.array(dists)

def get_distribution(n):
    dist=np.random.rand(n)
    c=sum(dist)
    dist/=c
    return dist
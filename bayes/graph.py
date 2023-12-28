import copy

class SimpleDiGraph(object):
    def __init__(self,n_nodes:int):
        self.in_edges=[[] for i in range(n_nodes)]
        self.out_edges=[[] for i in range(n_nodes)]
    
    def nodes(self):
        return range(len(self.in_edges))

    def add_edge(self,start,end):
        self.in_edges[start].append(end)
        self.out_edges[end].append(start)
    

    def input_nodes(self):
        in_nodes=[]
        for i,edge_i in enumerate(self.out_edges):
            if(len(edge_i)==0):
                in_nodes.append(i)
        return in_nodes

    def topological_sort(self):
        S=self.input_nodes()
        L=[]
        edges=copy.deepcopy(self.in_edges)
        while S:
            node_i=S.pop()
            L.append(node_i)
            for j,edge_j in enumerate(self.in_edges[node_i]):
                print("OK")
                print(edge_j)
#                del edges[node_i][j]
#                if(len(edges[node_i])==0):
#                    S.append(node_i)
        return L 
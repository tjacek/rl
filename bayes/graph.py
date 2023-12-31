import copy

class SimpleDiGraph(object):
    def __init__(self,start_edges,end_edges=None):
        if(end_edges is None):
            end_edges=[[] for i in range(start_edges)]
            start_edges=[[] for i in range(start_edges)]
        self.start_edges=start_edges
        self.end_edges=end_edges
    
    def nodes(self):
        return range(len(self.start_edges))

    def add_edge(self,start,end):
        self.start_edges[start].append(end)
        self.end_edges[end].append(start)

    def remove_edge(self,start,end):
        self.start_edges[start].remove(end)
        self.end_edges[end].remove(start)
    
    def input_nodes(self):
        in_nodes=[]
        for i,edge_i in enumerate(self.end_edges):
            if(len(edge_i)==0):
                in_nodes.append(i)
        return in_nodes
    
    def copy(self):
        start=copy.deepcopy(self.start_edges)
        end=copy.deepcopy(self.end_edges)
        return SimpleDiGraph(start_edges=start,
                             end_edges=end)

    def print(self):
        print(f'start:{self.start_edges}')
        print(f'end:{self.end_edges}')

    def topological_sort(self):
        S=self.input_nodes()
        L=[]
        graph=self.copy()
        while S:
            n=S.pop()
            L.append(n)
            for m in self.start_edges[n]:
                graph.remove_edge(n,m)
                if(len(graph.end_edges[m])==0):
                    S.append(m)
        return L 
#include "bayes.h"

Graph::Graph(int size){
  for(int i=0;i<size;i++){
    std::vector<int> near_i;
    this->near.push_back(near_i);
  }
}

void Graph::add_edge(int i,int j){
  this->start_edges[i].push_back(j);
  this->end_edges[j].push_back(i);
}

std::vector<int> input_nodes(){
  std::vector<int> input;
  int i=0;
  for(auto edge_i :this->end_edges){
    if(edge_i.size()==0){
      input.push_back(i);
    }
    i++;
  }
  return input;
}


std::vector<int> topological_sort(){
  std::vector<int> ordering;
  return ordering;
}

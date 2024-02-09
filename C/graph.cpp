#include "bayes.h"

Graph::Graph(int size){
  for(int i=0;i<size;i++){
    std::vector<int> near_i;
    this->near.push_back(near_i);
  }
}

void Graph::add_edge(int i,int j){
  this->near[i].push_back(j);
  this->near[j].push_back(i);
}

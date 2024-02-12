#include "bayes.h"

Graph::Graph(int size){
  for(int i=0;i<size;i++){
    std::vector<int> near_i;
    this->start_edges.push_back(near_i);
    this->end_edges.push_back(near_i);
  }
}

Graph::Graph(Graph &t){

}

void Graph::add_edge(int i,int j){
  this->start_edges[i].push_back(j);
  this->end_edges[j].push_back(i);
}

std::vector<int> Graph::input_nodes(){
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


std::vector<int> Graph::topological_sort(){
  std::vector<int> ordering;
  std::vector<int> input_nodes=this->input_nodes();
  while(!input_nodes.empty()){
    int n=input_nodes.back();
    input_nodes.pop_back();
    std::cout << n <<"\n";
  }
  return ordering;
}

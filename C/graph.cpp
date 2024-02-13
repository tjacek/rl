#include "bayes.h"

Graph::Graph(int size){
  for(int i=0;i<size;i++){
    std::vector<int> near_i;
    this->start_edges.push_back(near_i);
    this->end_edges.push_back(near_i);
  }
}

Graph::Graph(Graph &g){
 for(int i=0;i<g.start_edges.size();i++){
   std::vector<int> start_i;
   for(int j=0;j<g.start_edges[i].size();j++){
     start_i.push_back(g.start_edges[i][j]);
   }
   this->start_edges.push_back(start_i);
   std::vector<int> end_i;
   for(int j=0;j<g.end_edges[i].size();j++){
     end_i.push_back(g.end_edges[i][j]);
   }
   this->end_edges.push_back(end_i);
 }
}

int Graph::size(){
  return this->start_edges.size();
}

void Graph::add_edge(int i,int j){
  this->start_edges[i].push_back(j);
  this->end_edges[j].push_back(i);
}

void Graph::remove_edge(int i,int j){
//  vec.erase(std::remove(vec.begin(), vec.end(), 8), vec.end());
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
  Graph g=*this;
  while(!input_nodes.empty()){
    int n=input_nodes.back();
    input_nodes.pop_back();
    std::cout << n <<"\n";
  }
  return ordering;
}

std::string Graph::to_str(){
  std::string str;
  std::ostringstream stream;
  for(int i=0;i<this->size();i++){
    for(int j=0;j<this->start_edges[i].size();j++){
      stream << this->start_edges[i][j] <<",";
    }
    stream << "|";
    for(int j=0;j<this->end_edges[i].size();j++){
      stream << this->end_edges[i][j] <<",";
    }
    if(!this->start_edges[i].empty() ||
        !this->end_edges[i].empty()){
      stream << "\n";
    }
  }
  return stream.str();
}

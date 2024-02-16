#include "bayes.h"

Graph::Graph(int size){
  for(int i=0;i<size;i++){
    std::list<int> near_i;
    this->start_edges.push_back(near_i);
    this->end_edges.push_back(near_i);
  }
}

Graph::Graph(Graph &g){
  for(int i=0;i<g.start_edges.size();i++){
    std::list<int> start_i;
    for(auto j:g.start_edges[i]){
      start_i.push_back(j);
    }
    this->start_edges.push_back(start_i);
    std::list<int> end_i;
    for(auto j:g.end_edges[i]){
      end_i.push_back(j);
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

void Graph::remove_edge(int start,int end){
  this->start_edges[start].remove(end);
  this->end_edges[end].remove(start);
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

void show(std::vector<int> ordering){
  for(auto i:ordering){
    std::cout << i << " ";
  }
  std::cout <<"\n";
}

std::vector<int> Graph::topological_sort(){
  std::vector<int> ordering;
  std::vector<int> input_nodes=this->input_nodes();
  Graph g=*this;
  while(!input_nodes.empty()){
    int n=input_nodes.back();
    input_nodes.pop_back();
    ordering.push_back(n);
    for(int m:this->start_edges[n]){
      g.remove_edge(n,m);
      if(g.end_edges[m].size()==0){
        input_nodes.push_back(m);
      }
    }
  }
  return ordering;
}

std::string Graph::to_str(){
  std::string str;
  std::ostringstream stream;
  for(int i=0;i<this->size();i++){
    for(auto j:this->start_edges[i]){
      stream << j <<",";
    }
    stream << "|";
    for(auto j:this->end_edges[i]){
      stream << j  << ",";
    }
    if(!this->start_edges[i].empty() ||
        !this->end_edges[i].empty()){
      stream << "\n";
    }
  }
  return stream.str();
}

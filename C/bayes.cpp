#include "bayes.h"

void test_product(){
  FactorPtr A= read_factor("A.txt");
  FactorPtr B= read_factor("B.txt");
  FactorPtr C=A->product(B);
  std::cout << C->to_str();
}

int main(){
  Graph graph(5);
  graph.add_edge(0,2);
  graph.add_edge(1,2);
  graph.add_edge(2,3);
  graph.add_edge(2,4);
  graph.topological_sort();
//  FactorPtr factor= read_factor("fac.txt");

//  FactorPtr factor= read_factor("fac.txt");
//  std::cout << factor->to_str();
//  FactorPtr f=factor->marginalize("Y");
//  std::cout << "*************\n";
}
#include "bayes.h"

void test_product(){
  FactorPtr A= read_factor("A.txt");
  FactorPtr B= read_factor("B.txt");
  FactorPtr C=A->product(B);
  std::cout << C->to_str();
}

void test_graph(){
  Graph graph(5);
  graph.add_edge(0,2);
  graph.add_edge(1,2);
  graph.add_edge(2,3);
  graph.add_edge(2,4);
  std::cout << graph.to_str();
}

void battery(){
  BayesNet bn(5);
  VariablePtr B(new Variable("B",2));
  VariablePtr S(new Variable("S",2));
  VariablePtr E(new Variable("E",2));
  VariablePtr D(new Variable("D",2));
  VariablePtr C(new Variable("C",2));
  bn.variables.push_back(B);
  bn.variables.push_back(S);
  bn.variables.push_back(E);
  bn.variables.push_back(D);
  bn.variables.push_back(C);
  bn.graph.add_edge(0,2);
  bn.graph.add_edge(1,2);
  bn.graph.add_edge(2,3);
  bn.graph.add_edge(2,4);
  bn.factors.push_back(read_factor("battery/B.txt"));
  bn.factors.push_back(read_factor("battery/S.txt"));
  bn.factors.push_back(read_factor("battery/EBS.txt"));
  bn.factors.push_back(read_factor("battery/DE.txt"));
  bn.factors.push_back(read_factor("battery/CE.txt"));
}

int main(){
  battery();
//  FactorPtr factor= read_factor("fac.txt");

//  FactorPtr factor= read_factor("fac.txt");
//  std::cout << factor->to_str();
//  FactorPtr f=factor->marginalize("Y");
//  std::cout << "*************\n";
}
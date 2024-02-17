#include "infer.h"


FactorPtr WeightedSampling::operator()(BayesNet & bn,Query query,Evidence evidence){
  FactorPtr factor=std::make_shared<Factor>();
  std::vector<int> ordering = bn.graph.topological_sort();
  return factor; 
}
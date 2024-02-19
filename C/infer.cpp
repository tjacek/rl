#include "infer.h"


FactorPtr WeightedSampling::operator()(BayesNet & bn,Query query,Evidence evidence){
  FactorPtr factor=std::make_shared<Factor>();
  std::vector<int> ordering = bn.graph.topological_sort();
  for(int i=0;i<this->m;i++){
    AssigPtr a_i=std::make_shared<Assig>();
    double w_i=1.0;
    for(int j:ordering){
      std::string name_j=bn.variables[j]->name;
      FactorPtr theta_j=bn.factors[j];
      if(evidence->dict.contains(name_j)){
        a_i->dict[name_j]=evidence->dict[name_j];
        AssigPtr a_j=a_i->select(theta_j->variable_names());
        w_i*=theta_j->table.get(a_j);
      }else{
         AssigPtr rand_a=theta_j->condition(a_i)->sample();
         a_i->dict[name_j]=rand_a->dict[name_j];
      }
    }
    AssigPtr b_i=a_i->select(query);
    double value_i=factor->table.get(b_i)+w_i;
    factor->table.set(b_i,value_i);
//    std::cout << a_i->to_str() <<"\n";
  }
  std::unordered_set<std::string> query_set(std::begin(query),std::end(query));;
  for(auto var_i:bn.variables){
    if(query_set.contains(var_i->name)){
      factor->variables.push_back(var_i);
    }
  }
  factor->normalize();
  return factor; 
}
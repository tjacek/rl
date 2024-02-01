#include "bayes.h"

std::string Assig::to_id(){
  std::string id="";
  for (auto pair_i : this->dict){
  	id+= std::to_string(pair_i.second);
  }
  return id;
}

std::string Assig::to_str(){
  std::string id="";
  for (auto pair_i : this->dict){
  	id+= pair_i.first;
  	id+="=";
  	id+= std::to_string(pair_i.second);
  	id+=",";
  }
  return id;
}

double Table::get(Assig & assig){
  std::string id=assig.to_id();
  if( this->dict.contains(id)){
    return this->dict[id];
  }
  return 0.0;
}

void Table::set(Assig & assig,double p){
  std::string id=assig.to_id();
  this->dict[id]=p;
}

double Table::sum(){
  double total=0.0;
  for (auto pair_i : this->dict){
  	total+= pair_i.second;
  }
  return total;
}

std::list<std::string> Factor::variable_names(){
  std::list<std::string> names;
  for(const auto& variable_i : this->variables){
    names.push_back(variable_i->name);
  }
  return names;
}

bool Factor::in_scope(std::string name){
  for(const auto& variable_i : this->variables){
    if(variable_i->name==name){
      return true;
    }
  }
  return false;
}

FactorPtr Factor::condition(Assig & evidence){
  FactorPtr theta(this);
  for (auto pair_i : evidence.dict){
    theta=this->condition(theta,pair_i.first,pair_i.second);
  }
  return theta;
}


FactorPtr Factor::condition(FactorPtr factor,std::string name,double value){
  if( factor->in_scope(name)){
    return factor;
  }
//  std::list<Variable> vars;
  auto theta = std::make_shared<Factor>();
  
  for(const auto& variable_i : this->variables){
    if(variable_i->name==name){
      theta->variables.push_back(variable_i);
    }
  }
  return theta;
}

FactorPtr read_factor(std::string name){
  FactorPtr theta = std::make_shared<Factor>();
  std::ifstream infile(name);
  std::string line;
  while (std::getline(infile, line)){
    if(theta->variables.empty()){
      std::vector<std::string> var_names=split(line);
      for(auto name_j : var_names){
        VariablePtr var_j(new Variable(name_j));
        theta->variables.push_back(var_j);
      }
      std::cout  << line << "\n";
    } 
  }
  return theta;
}

std::vector<std::string> split(std::string str){
  std::vector<std::string> v;
  std::stringstream ss(str);
  while (ss.good()) {
    std::string substr;
    getline(ss, substr, ',');
    v.push_back(substr);
  }
  return v;
}

int main(){
// Assig assig;
// assig.dict={{"B", 1}, 
//             {"A", 0}, 
//             {"C", 1}};
// std::cout << assig.to_str() << "\n";
  read_factor("fac.txt");
}
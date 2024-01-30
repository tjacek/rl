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
    names.push_back(variable_i.name);
  }
  return names;
}


int main(){
 Assig assig;

 assig.dict={{"B", 1}, 
             {"A", 0}, 
             {"C", 1}};
 std::cout << assig.to_str() << "\n";
}
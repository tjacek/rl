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

int main(){
 Assig assig;

 assig.dict={{"B", 1}, 
             {"A", 0}, 
             {"C", 1}};
 std::cout << assig.to_str() << "\n";
}
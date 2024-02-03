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

void Table::set(std::vector<int> assig,double p){
  std::string id="";
  for (auto value_i : assig){
    id+= std::to_string(value_i);
  }
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
  auto theta = std::make_shared<Factor>();
  
  for(const auto& variable_i : this->variables){
    if(variable_i->name==name){
      theta->variables.push_back(variable_i);
    }
  }
  return theta;
}

std::string Factor::to_str(){
  std::string id="";
  for (auto pair_i : this->table.dict){
    int j=0;
    std::string line_j="";
    for(auto v_j: this->variables){
      line_j+= v_j->name + "=" + pair_i.first[j]+",";
      j++; 
    }
    id+=line_j+":"+std::to_string(pair_i.second)+"\n";
  }
  return id;
}

FactorPtr read_factor(std::string name){
  FactorPtr theta = std::make_unique<Factor>();
  std::ifstream infile(name);
  std::string line;
  while (std::getline(infile, line)){
    if(theta->variables.empty()){
      std::vector<std::string> var_names=split(line);
      for(auto name_j : var_names){
        VariablePtr var_j(new Variable(name_j));
        theta->variables.push_back(var_j);
      }
     
    }else{
       std::vector<std::string> raw=split(line);   
       std::vector<int> assig;
       for(int i=0; i<raw.size()-1; i++){
         assig.push_back(stoi(raw[i]));
       }
       double p= std::stod(raw[raw.size()-1]);
       theta->table.set(assig,p);
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
  FactorPtr factor= read_factor("fac.txt");
  std::cout << factor->to_str();
}
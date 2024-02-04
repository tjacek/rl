#include "bayes.h"

std::string Assig::to_id(){
  std::string id="";
  for (auto pair_i : this->dict){
  	id+= std::to_string(pair_i.second);
  }
  return id;
}

AssigPtr Assig::del(std::string name){
  AssigPtr new_assig=std::make_shared<Assig>();
  for (auto pair_i : this->dict){
    if(pair_i.first!=name){
//      new_assig->dict[pair_i.first]=pair_i.second;
    }
  }
  return new_assig;
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

double Table::get(AssigPtr assig){
  std::string id=assig->to_id();
  if( this->prob_dict.contains(id)){
    return this->prob_dict[id];
  }
  return 0.0;
}

void Table::set(AssigPtr assig,double p){
  std::string id=assig->to_id();
  this->assig_dict[id]=assig;
  this->prob_dict[id]=p;
}

void Table::set(std::list<VariablePtr> & variables,std::vector<int> values,double p){
  AssigPtr assig(new Assig());
  int i=0;
  for(auto var_i:variables){
    assig->dict[var_i->name]=values[i];
    i++;
  }
  std::string id=assig->to_id();
  this->assig_dict[id]=assig;
  this->prob_dict[id]=p;
}

double Table::sum(){
  double total=0.0;
  for (auto pair_i : this->prob_dict){
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

FactorPtr Factor::condition(AssigPtr evidence){
  FactorPtr theta=std::make_shared<Factor>(*this);
  for (auto pair_i : evidence->dict){
    theta=theta->condition(pair_i.first,pair_i.second);
  }
  return theta;
}

FactorPtr Factor::condition(std::string name,int value){
  if( !this->in_scope(name)){
    return std::make_shared<Factor>(*this);
  }
  auto theta = std::make_shared<Factor>();
  for(auto pair_i : this->table.assig_dict){
    if(pair_i.second->dict[name]==value){
      AssigPtr assig=pair_i.second->del(name);
      std::string id=pair_i.second->to_id();    
//      theta->table.assig_dict[id]=assig;
      std::cout << id << " " << assig->to_id() <<"\n";
      double p_i=this->table.prob_dict[id];
      theta->table.prob_dict[id]=p_i;
    }
  }
  for(const auto& variable_i : this->variables){
    if(variable_i->name!=name){
      theta->variables.push_back(variable_i);
    }
  }
  return theta;
}

std::string Factor::to_str(){
  std::string id="";
  for(auto var_i : this->variables){
    id+=var_i->name +" ";
  }
  id+="\n";
  for (auto pair_i : this->table.prob_dict){
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
       theta->table.set(theta->variables,assig,p);
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
  AssigPtr evidence(new Assig({{"Y", 1}}));
  FactorPtr f=factor->condition(evidence);
  std::cout << "*************\n";
  std::cout << f->to_str();
}
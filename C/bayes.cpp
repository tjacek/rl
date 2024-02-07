#include "bayes.h"

std::vector<VariablePtr> var_diff(std::vector<VariablePtr> & theta, 
                                  std::vector<VariablePtr> & psi){
  std::unordered_set<std::string> theta_names;
  for(auto var_i :theta){
    theta_names.insert(var_i->name);
  }
  std::vector<VariablePtr> psi_only;
  for(auto var_i :psi){
    if(!theta_names.contains(var_i->name)){
      std::cout << var_i->name;
      psi_only.push_back(var_i);
    }
  }
  return psi_only;
}

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
      new_assig->dict[pair_i.first]=pair_i.second;
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

std::vector<AssigPtr> assignments(std::vector<VariablePtr> variables){
  std::vector<AssigPtr> all_assig;
  std::vector<int> curent(variables.size(), 0);
  bool more=true;
  AssigPtr a_i=std::make_shared<Assig>();
  while(more){
    for(int j=0;j<variables.size();j++){
      a_i->dict[variables[j]->name]=curent[j];
    }
    more=false;
    for(int j=0;j<curent.size()-1;j++){
      if(curent[j]<variables[j]->domian){
        curent[j]+=1;
        more=true;
        break;
      }else{
        curent[j]=0;
      }
    }
//    for(int j=0;j<curent.size();j++){
//      std::cout << curent[j] << " ";
//    }
    std::cout << a_i->to_str() <<"\n";
  }
  return all_assig;
}


std::vector<std::string> Table::keys(){
  std::vector<std::string> keys;
  keys.reserve(this->prob_dict.size());
  for(const auto& [key, value] : this->prob_dict) {
    keys.push_back(key);
  }
  return keys;
}

double Table::get(AssigPtr assig){
  std::string id=assig->to_id();
  if( this->prob_dict.contains(id)){
    return this->prob_dict[id];
  }
  return 0.0;
}

std::pair<AssigPtr,double> Table::get(std::string name){
  return std::make_pair(this->assig_dict[name],this->prob_dict[name]);
}


void Table::set(AssigPtr assig,double p){
  std::string id=assig->to_id();
  this->assig_dict[id]=assig;
  this->prob_dict[id]=p;
}

void Table::set(std::vector<VariablePtr> & variables,std::vector<int> values,double p){
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

std::vector<std::string> Factor::variable_names(){
  std::vector<std::string> names;
  for(const auto& variable_i : this->variables){
    names.push_back(variable_i->name);
  }
  return names;
}

std::unordered_set<std::string> Factor::variable_set(){
  std::vector<std::string> names=this->variable_names();
  std::unordered_set<std::string> name_set(std::begin(names), std::end(names));;
  return name_set;
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
      double p_i=this->table.prob_dict[id];
      theta->table.prob_dict[assig->to_id()]=p_i;
    }
  }
  for(const auto& variable_i : this->variables){
    if(variable_i->name!=name){
      theta->variables.push_back(variable_i);
    }
  }
  return theta;
}

FactorPtr Factor::marginalize(std::string name){
  FactorPtr theta = std::make_shared<Factor>();
  for(auto var_i : this->variables){
    if(var_i->name != name){
      theta->variables.push_back(var_i);
    }
  }
  for(auto pair_i : this->table.assig_dict){
    AssigPtr a_i= pair_i.second;
    AssigPtr new_a_i= a_i->del(name);
    double curent_i=theta->table.get(new_a_i);
    double p_i=this->table.get(a_i);
    theta->table.set(new_a_i,curent_i+p_i);
  }
  return theta;
}

FactorPtr Factor::product(FactorPtr psi){
  std::vector<VariablePtr> psi_only=var_diff(this->variables,psi->variables);
  FactorPtr prod_factor = std::make_shared<Factor>();
  for (auto name_i : this->table.keys()){
    std::pair<AssigPtr,double> pair_i= this->table.get(name_i);
    std::vector<AssigPtr> assg_i=assignments(this->variables);
  }
  return prod_factor;
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
  FactorPtr A= read_factor("A.txt");
  FactorPtr B= read_factor("B.txt");
  FactorPtr C=A->product(B);
//  FactorPtr factor= read_factor("fac.txt");

//  FactorPtr factor= read_factor("fac.txt");
//  std::cout << factor->to_str();
//  FactorPtr f=factor->marginalize("Y");
//  std::cout << "*************\n";
  std::cout << C->to_str();
}
#include <string>
#include <iostream>
#include <list>
#include <map>

class Variable{
  public:
  	std::string name;
  	int domian;
};

class Assig{
  public:
    std::map<std::string,int> dict;
    std::string to_id();
    std::string to_str();

};

//class FactorTable{
//  std::map<std::string,Assig>;
//  public:
//  	 double get(Assig assig);
//  	 void set(Assig assig,double p);
//  	 double sum();
//};

//class Factor{
//  std::list<Variable> variables;
//  FactorTable table;
//  std::list<std::string> variable_names();
//  bool in_scope(std::string name);
//  Factor condition(Assig evidence);
//  Factor marginalize(std::string name);
//};
#include <string>
#include <iostream>
#include <list>
#include <map>
#include <memory>

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

class Table{
  std::map<std::string,double> dict;
  public:
  	 double get(Assig & assig);
  	 void set(Assig & assig,double p);
  	 double sum();
};

class Factor;
typedef std::shared_ptr<Factor> FactorPtr;

class Factor{
  std::list<Variable> variables;
  Table table;
  std::list<std::string> variable_names();
  bool in_scope(std::string name);
  FactorPtr condition(Assig & evidence);
  FactorPtr condition(FactorPtr factor,std::string name,double value);
  FactorPtr marginalize(std::string & name);
};


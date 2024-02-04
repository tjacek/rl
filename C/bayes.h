#include <string>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <memory>
#include <fstream>
#include <sstream>

class Variable{
  public:
  	std::string name;
  	int domian=2;
};

typedef std::shared_ptr<Variable> VariablePtr;

class Assig;
typedef std::shared_ptr<Assig> AssigPtr;

class Assig{
  public:
    std::map<std::string,int> dict;
    std::string to_id();
    std::string to_str();
    AssigPtr del(std::string name);
};

class Table{
  public:
    std::map<std::string,double> prob_dict;
    std::map<std::string,AssigPtr> assig_dict;
    
    double get(AssigPtr assig);
    void set(AssigPtr assig,double p);
    void set(std::list<VariablePtr> & variables,std::vector<int> values,double p);
    double sum();
};

class Factor;
typedef std::shared_ptr<Factor> FactorPtr;

class Factor{
  public:
    std::list<VariablePtr> variables;
    Table table;
    std::list<std::string> variable_names();
    bool in_scope(std::string name);
    FactorPtr condition(AssigPtr evidence);
    FactorPtr condition(std::string name,int value);
    FactorPtr marginalize(std::string & name);
    std::string to_str();
};

FactorPtr read_factor(std::string name);
std::vector<std::string> split(std::string str);
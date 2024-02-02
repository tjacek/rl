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

class Assig{
  public:
    std::map<std::string,int> dict;
    std::string to_id();
    std::string to_str();

};

//typedef std::shared_ptr<Assig> AssigPtr;

class Table{
  public:
    std::map<std::string,double> dict;
    double get(Assig & assig);
    void set(Assig & assig,double p);
    void set(std::vector<int> assig,double p);
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
    FactorPtr condition(Assig & evidence);
    FactorPtr condition(FactorPtr factor,std::string name,double value);
    FactorPtr marginalize(std::string & name);
};

FactorPtr read_factor(std::string name);
std::vector<std::string> split(std::string str);
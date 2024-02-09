#include <string>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <unordered_set>
#include <memory>
#include <fstream>
#include <sstream>

class Variable{
  public:
  	std::string name;
  	int domian=2;
};

typedef std::shared_ptr<Variable> VariablePtr;

std::vector<VariablePtr> var_diff(std::vector<VariablePtr>& base, 
                                  std::vector<VariablePtr>& other);

class Assig;
typedef std::shared_ptr<Assig> AssigPtr;

class Assig{
  public:
    std::map<std::string,int> dict;
    std::string to_id();
    std::string to_str();
    AssigPtr del(std::string name);
    AssigPtr select(std::vector<std::string> names);
};

std::vector<AssigPtr> assignments(std::vector<VariablePtr> variables);
AssigPtr merge(AssigPtr a, AssigPtr b);

class Table{
  public:
    std::map<std::string,double> prob_dict;
    std::map<std::string,AssigPtr> assig_dict;
    
    std::vector<std::string> keys();
    double get(AssigPtr assig);
    std::pair<AssigPtr,double> get(std::string name);
    void set(AssigPtr assig,double p);
    void set(std::vector<VariablePtr> & variables,std::vector<int> values,double p);
    double sum();
};

class Factor;
typedef std::shared_ptr<Factor> FactorPtr;

class Factor{
  public:
    std::vector<VariablePtr> variables;
    Table table;
    std::vector<std::string> variable_names();
    std::unordered_set<std::string> variable_set();

    bool in_scope(std::string name);
    FactorPtr condition(AssigPtr evidence);
    FactorPtr condition(std::string name,int value);
    FactorPtr marginalize(std::string name);
    FactorPtr product(FactorPtr ptr);
    std::string to_str();
};

FactorPtr read_factor(std::string name);
std::vector<std::string> split(std::string str);

class Graph{
  public:
    std::vector<std::vector<int>> near;
    Graph(int size);
    void add_edge(int i,int j);
};

class BayesNet{
  public:
    std::vector<VariablePtr> variables;
    std::vector<FactorPtr> factors;
    Graph graph;
};
#include "bayes.h"

typedef std::vector<std::string> Query;
typedef AssigPtr Evidence;


class Sampling{
 public:
   virtual FactorPtr operator()(BayesNet & bn,Query query,Evidence evidence)=0;
};

class WeightedSampling:Sampling{
  public:
    int m;
    WeightedSampling(int m):m(m){};
    FactorPtr operator()(BayesNet & bn,Query query,Evidence evidence);
};
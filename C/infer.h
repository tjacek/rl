#include "bayes.h"

typedef std::vector<VariablePtr> Query;
typedef AssigPtr Evidence;


class InferAlg{
 FactorPtr opearator()(BayesNet & bn,Query query,Evidence evidence);
};
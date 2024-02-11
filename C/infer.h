#include "bayes.h"

typedef std::vector<VariablePtr> Query;
typedef AssigPtr Evidence;


class InferAlg{
 FactorPtr infer(Query query,Evidence evidence);
};
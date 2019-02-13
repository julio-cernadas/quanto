#include "Stats.h"
#include "Utils.h"

double Stats::VAI(const vector_2D<double>& v)
{
    int n = v.size();                   // Declare an unsigned integer
    double vai;                         // Define a double for VAI
    vai = 1000.0;                       // Initialise to $1,000
    for(int i = 0; i != n; ++i) {       // Calculate VAI using Eqn. (3.1)
        vai *= (1 + v[i][v[0].size()-1] / 100.0);
    }
    return vai; 
}


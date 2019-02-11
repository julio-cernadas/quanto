#include "Stats.h"
#include "Utils.h"

DBL Stats::VAI(const V2DD& v)
{
    UINT n = v.size();          // Declare an unsigned integer
    DBL vai;                    // Define a double for VAI
    vai = 1000.0;               // Initialise to $1,000
    for(UINT i=0; i<n; i++) {   // Calculate VAI using Eqn. (3.1)
        vai *= (1 + v[i][v[0].size()-1] / 100.0);
    }
    return vai; 
}

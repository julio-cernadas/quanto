#include "Import.h"
#include "Utils.h"
#include "Stats.h"

#include <iostream>
#include <string>
#include <memory>
#include <vector>

using std::cout;
using std::cin;

int main() 
{
    V2DD data;                  // Declare a 2D vector for the data values
    Import ctai;                // Create an instance of the Import class
    
    // Call GetData() member function from the Import class
    data = ctai.GetData("gold.dat");

    Stats stats;
    DBL vai;
    vai = stats.VAI(data);

    cout << "\n VAI($): " << vai << "\n"; 
    cin.get();
    return 0; 
}
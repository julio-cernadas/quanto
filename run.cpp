#include "Stock.h"
#include "Utils.h"
#include "Stats.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <memory>
#include <vector>

using std::cout, std::cin, std::string, std::vector;

int main() 
{
    vector_2D<string> data;
    string fileName = "AAL.csv";
    Stock aal_stock;
    data = aal_stock.get_data(fileName);
    Utils::print_data(data,25);
    return 0;
}

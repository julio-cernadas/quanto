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
    vector_2D<string> prev_data;
    vector_2D<double> data;
    string fileName = "AAL.csv";
    Stock aal_stock;
    prev_data = aal_stock.prev_data(fileName);
    data      = aal_stock.get_data(prev_data);
    Utils::print_data(data,10);
    return 0;
}


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
    vector_2D<string> raw_data;
    vector_2D<double> data;

    string fileName = "AAL.csv";
    Stock aal_stock;
    Stats stats;
    raw_data = aal_stock.raw_data(fileName);
    data = aal_stock.get_data(raw_data);
    aal_stock.add_daily_change(data);

    Utils::print_data(data,50);
    double mean = stats.get_standard_dev(data);
    cout << mean;
    return 0;
}


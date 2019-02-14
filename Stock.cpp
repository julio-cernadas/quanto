#include "Stock.h"

#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <boost/algorithm/string.hpp>

using std::cout;
using std::cin;
using std::string;
using std::vector;

vector_2D<string> Stock::raw_data(const string& fileName) 
{   
    string line, tmp;                      
    std::ifstream file(fileName);       // incoming file stream to go...
    vector_2D<string> data;
    while (std::getline(file,line)) {
        vector<string> vec;
        boost::algorithm::split(vec, line, boost::is_any_of(","));
        data.push_back(vec);
    }
    return data;
}

vector_2D<double> Stock::get_data(vector_2D<string> data)
{  
    data.erase(data.begin());
    vector_2D<double> vec2D;
    for (auto row : data) {   // for each row in data
        vector<double> vec(row.size() - 1);
        std::transform(std::next(row.begin()), row.end(), vec.begin(), 
            [](string const& val) {
                return stod(val);
            }
        );
        vec2D.push_back(vec);
    }
    return vec2D;
}

void Stock::add_daily_change(vector_2D<double>& data)
{
    double change;
    for (auto& row : data) {
        change = (row[3] - row[0]) / row[0];
        row.push_back(change);
    }
}

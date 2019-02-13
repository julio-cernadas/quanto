#include "Stock.h"

#include <fstream>
#include <sstream>
#include <iostream>
#include <boost/algorithm/string.hpp>

using std::cout;
using std::cin;
using std::string;
using std::vector;

vector_2D<string> Stock::get_data(const string& fileName) 
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

vector_2D<double> Stock::clean_data(vector_2D<string>& data)
{
    // TODO: 
    // - Convert a string vector to a double vector with just nums
    // - Create Stat methods such as mean and standard dev.




}


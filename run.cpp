#include "Import.h"
#include "Utils.h"
#include "Stats.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <memory>
#include <vector>
#include <boost/algorithm/string.hpp>

using std::cout, std::cin, std::string, std::vector;

//vector_2D<double>
void get_data(const string& fileName) 
{   
    int rows = 0, cols = 0;             // setting up for file input
    string line, tmp;                      
    vector<string> titles;
    std::ifstream file(fileName);       // incoming file stream to go...
    vector_2D<string> data;
    while (std::getline(file,line)) {
        vector<string> vec;
        boost::algorithm::split(vec, line, boost::is_any_of(","));
        data.push_back(vec);
    }

}


int main() 
{
    string fileName = "AAL.csv";
    get_data(fileName);
    return 0;
}

    // vector_2D<double> data;     // Declare a 2D vector for the data values
    // Import ctai;                // Create an instance of the Import class
    
    // // Call GetData() member function from the Import class
    // data = ctai.GetData("gold.dat");

    // vector<string> v;
    // v.push_back("CTA");

    // cout << "\n Printing first 18:\n";
    // Utils::PrintFile(data, v, 18); 
    // cin.get();
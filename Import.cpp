#include "Import.h"

#include <fstream>
#include <sstream>
#include <iostream>

using std::cout;
using std::cin;
using std::string;
using std::vector;

vector_2D<double> Import::GetData(const std::string& fileName)
{
    int ROW = 0, COLS = 0;            // Initialise rows and columns
    string line, tmp;
    std::stringstream ss;            // Create a stringstream object
    std::ifstream file(fileName);    // Add file to fstream
    std::getline(file, line);        // Remove file header
    ss.clear();                      // Clear stringstream
    ss << line;
    while (ss >> tmp) {
            COLS++;             // Determine # columns (COLS) in file
    }
    vector_2D<double> data;                  // Declare a 2D vector of doubles
    vector<double> v(COLS);               // Declare a 1D vector of doubles

    if (file.is_open()) {
        while(file.good()) {
            data.push_back(v);  // Add a new row to data
            for (int COL = 0; COL != COLS; ++COL) {
                    file >> data[ROW][COL];     // Fill the row with COL elements
            }
            ROW++;              // Keep track of the current ROW and increment
        }
        data.pop_back();            // Remove null values at end of data...
        cout << "\n File:" << fileName << "\n";
        cout << " Imported " << data.size() * (COLS - 1) << " value successfully!\n";
        file.close(); // Close file
    } 
    else {
        m_utils.ErrorChk("Unable to load file");
    }
    return data;
}
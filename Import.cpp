#include "Import.h"

#include <fstream>
#include <sstream>
#include <iostream>

using std::cout;
using std::string;
using std::ifstream;
using std::stringstream;

V2DD Import::GetData(const string& fileName)
{
    int ROW = 0, COLS = 0;      // Initialise rows and columns
    string line, tmp;
    stringstream ss;            // Create a stringstream object
    ifstream file(fileName);    // Add file to fstream
    getline(file, line);        // Remove file header
    ss.clear();                 // Clear stringstream
    ss << line;
    while (ss >> tmp) {
            COLS++;             // Determine # columns (COLS) in file
    }
    V2DD data;                  // Declare a 2D vector of doubles
    V1DD v(COLS);               // Declare a 1D vector of doubles

    if(file.is_open()) {
        while(file.good()) {
            data.push_back(v);  // Add a new row to data
            for (int COL = 0; COL != COLS; ++COL) {
                    file >> data[ROW][COL];     // Fill the row with COL elements
            }
            ROW++;              // Keep track of the current ROW and increment
        }
        data.pop_back();            // Remove null values at end of data...
        std::cout << "\n File:" << fileName << "\n";
        std::cout << " Imported " << data.size() * (COLS - 1) << " value successfully!\n";
        file.close(); // Close file
    } 
    else {m_utils.ErrorChk("Unable to load file");}
    return data;
}
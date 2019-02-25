#include "Utils.h"

#include <iostream>
#include <iomanip>
#include <cmath>

using std::cout;
using std::cin;
using std::string;
using std::vector;

void Utils::print_data(const vector_2D<string>& v, const int& n)
{
    for(int i = 0; i != n; ++i) {
        for(int j = 0; j < v[0].size(); ++j) {
            cout << std::left << "\t" << std::setw(6) << v[i][j];
        }
        cout << "\n";
    }
}

void Utils::print_data(const vector_2D<double>& v, const int& n)
{
    for(int i = 0; i != n; ++i) {
        for(int j = 0; j < v[0].size(); ++j) {
            cout << std::left << "\t" << std::setw(6) << v[i][j];
        }
        cout << "\n";
    }
}

void Utils::ErrorChk(const string& s)
{
    std::cerr << "\n Run-time error...\n"; 
    std::cerr << " Message: " << s << "\n\n"; 
    cin.get();
    exit(1);
}
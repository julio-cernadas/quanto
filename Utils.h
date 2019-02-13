#pragma once

#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::cin;
using std::string;
using std::vector;

// general 2-dimensional vector
template<typename T>
using vector_2D = vector<vector<T>>;

class Utils
{
private:
    // Member variable definitions 
public:
    // Constructor & Destructor
    Utils() {}  
    virtual ~Utils() {}

    // Static methods to be called... Utils::PrintFile
    static void PrintFile(const vector_2D<double>& v, 
                    const vector<string>& s, const int& n); 

    // Error Checking
    void ErrorChk(const string& s);
};
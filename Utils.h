#pragma once

#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;

typedef unsigned int UINT;
typedef double DBL;
typedef vector<int> V1DI;
typedef vector<float> V1DF;
typedef vector<string> V1DS;
typedef vector<double> V1DD;
typedef vector<vector<int>> V2DI;
typedef vector<vector<float>> V2DF;
typedef vector<vector<double>> V2DD;


class Utils
{
private:
    // Member variable definitions
public:
    Utils() {}
    virtual ~Utils() {}
    
    void PrintResult(const V1DD& v, const int& p, const V1DS& s, const int& WIDTH);
    static void PrintFile(const V2DD& v, const V1DS&, const int& n); 
    void ErrorChk(const string& s);
};
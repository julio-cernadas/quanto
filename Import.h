#pragma once

#include "Utils.h"
#include <string>

using std::string;

class Import
{
private:
    Utils m_utils;
public:
    Import() {}
    virtual ~Import() {}

    vector_2D<double> GetData(const string& fileName);
};

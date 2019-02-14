#pragma once

#include "Utils.h"
#include <string>

using std::string;

class Stock
{
private:
    Utils m_utils;
public:
    Stock() {}
    virtual ~Stock() {}

    vector_2D<string> raw_data(const string& fileName);
    vector_2D<double> get_data(vector_2D<string> data);
    void add_daily_change(vector_2D<double>& data);
};

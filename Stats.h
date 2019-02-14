#pragma once

#include "Utils.h"

class Stats
{
private:
    Utils m_utils;
public:
    Stats() {}                  // No ';' -> default constructor and
    virtual ~Stats() {}         // destructor...

    double get_returns_mean(vector_2D<double>& data);
    double get_standard_dev(vector_2D<double>& data);
};

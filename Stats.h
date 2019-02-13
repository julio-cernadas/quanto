#pragma once

#include "Utils.h"

class Stats
{
private:
    Utils m_utils;
public:
    Stats() {}                  // No ';' -> default constructor and
    virtual ~Stats() {}         // destructor...

    double VAI(const vector_2D<double>& v);     // VAI()
};

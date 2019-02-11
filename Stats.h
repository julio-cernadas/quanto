#pragma once

#include "Utils.h"

class Stats
{
private:
    Utils m_utils;
public:
    Stats() {}                  // No ';' -> default constructor and
    virtual ~Stats() {}         // destructor...

    DBL VAI(const V2DD& v);     // VAI()
};



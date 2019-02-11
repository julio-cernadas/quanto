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

    V2DD GetData(const string& fileName);
};

#include "Stats.h"

#include <cmath>

double Stats::get_returns_mean(vector_2D<double>& data)
{
    int n = data.size();
    double mean = 0.0;
    for (int i = 0; i != n; ++i) {
        mean += data[i][5];
    }
    mean /= n;
    return mean;
}

double Stats::get_standard_dev(vector_2D<double>& data)
{
    int n = data.size();
    double std = 0.0;
    double mean = get_returns_mean(data);
    for (int i = 0; i != n; ++i) {
        std += std::pow((data[i][data.size()-1] - mean),2);
    }
    return mean;
}


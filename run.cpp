#include "Stock.h"
#include "Utils.h"
#include "Stats.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <memory>
#include <vector>
#include <curl/curl.h>
#include "cJSON/cJSON.h"

using std::cout, std::cin, std::string, std::vector;

// int main() 
// {
//     vector_2D<string> raw_data;
//     vector_2D<double> data;

//     string fileName = "AAL.csv";
//     Stock aal_stock;
//     Stats stats;
//     raw_data = aal_stock.raw_data(fileName);
//     data = aal_stock.get_data(raw_data);
//     aal_stock.add_daily_change(data);

//     Utils::print_data(data,50);
//     double mean = stats.get_standard_dev(data);
//     cout << mean;

//     return 0;
// }

size_t writeFunction(void *ptr, size_t size, size_t nmemb, std::string* data) {
    data->append((char*) ptr, size * nmemb);
    return size * nmemb;
}



int main(int argc, char** argv) {
    auto curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol=MSFT");
        string response_string;
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writeFunction);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response_string);
        curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        cout << response_string << "\n";
    }
    return 0;
}
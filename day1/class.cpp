#include <iostream>
#include <string>
#include <sstream>
using namespace std;


int main(){


ostringstream str1;

int num = 2012;

str1<<num;
string num_string = str1.str();
cout<<num_string+num_string;

return 0;
}
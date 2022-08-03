/*
This short script shows the maximum limit of an integer, prints it and prints that integer plus 1 what causes a dataype overflow showing a negative number.
*/

#include <iostream>
#include <climits>

using namespace std;

int main()
{
    int inMax = INT_MAX;
    cout << inMax << endl;
    cout << inMax + 1;

    return 0;
}

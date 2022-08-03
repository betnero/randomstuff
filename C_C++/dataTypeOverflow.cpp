/*
This shortscript shows the maximum limit of an integer, printsit and prints that integer plus 1 what causes a dataype overflow printing a negative number.
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

#include <iostream>
#include <climits>
using namespace std;

//Check for even and odd numbers. If modulo is 0 the number is even.Else it is odd


int main()
{
    int number;
    cout << "Please enter full number: ";
    cin >> number;

    if(number % 2==0)
    {
    cout << "You have entered an even number." << endl;
    }

    else
    {
    cout << "You have entered n odd number." << endl;
    }
    cout << "Bye.";
    return 0;
}

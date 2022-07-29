#include <iostream>
#include <climits>
using namespace std;

//Number guessing game.

int main()
{
    int hostn, guestn;
    cout << "Host: ";
    cin >> hostn;
    system("cls");
    cout << "Guest: ";
    cin >> guestn;

    (hostn == guestn)? cout << "Correct!": cout << "Wrong!"; //Ternary operator in C++.

}

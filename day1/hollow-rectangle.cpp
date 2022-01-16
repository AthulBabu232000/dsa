#include <iostream>

using namespace std;

void hollowRectangle()
{
    int row, column, i, j;
    cout << "enter the row count: \n";
    cin >> row;
    cout << "\nenter the column count: \n";
    cin >> column;
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < column; j++)
        {
            if (i != 0 && j != 0 && i != row - 1 && j != column - 1)
            {
                cout << "   ";
            }
            else
            {
                cout << " * ";
            }
        }
        cout << "\n";
    }
}



void invertedPyramid()
{

    int n, i, j;

    cout << "enter the value of n: ";
    cin >> n;
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n - i + 1; j++)
        {
            cout << " * ";
        }
        cout << "\n";
    }

}
void halfPyramidRight(){
        int n, i, j;

    cout << "enter the value of n: ";
    cin >> n;
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n ; j++)
        {
            if(i + j <= n){
                cout<<"  ";
            }else{
                cout << " *";
            }
        }
        cout << "\n";
    }
}

int main()
{

    // hollowRectangle();
    // invertedPyramid();
halfPyramidRight();
    return 0;
}
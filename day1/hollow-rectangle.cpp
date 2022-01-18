#include <iostream>
#include <string>

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
void halfPyramidRight()
{
    int n, i, j;

    cout << "enter the value of n: ";
    cin >> n;
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
        {
            if (i + j <= n)
            {
                cout << "  ";
            }
            else
            {
                cout << " *";
            }
        }
        cout << "\n";
    }
}

void numberPyramid()
{
    int n, i, j;
    cout << "enter a number N: ";
    cin >> n;
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= i; j++)
        {
            cout << i;
        }
        cout << "\n";
    }
}

void floydTriangle()
{
    int n, i, j, count = 1;
    cout << "enter the value for n: " << endl;
    cin >> n;
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= i; j++)
        {
            cout << " " << count;
            count = count + 1;
        }
        cout << endl;
    }
}
void butterfly()
{
    int n, i, j;
    cout << "enter the value for n: ";
    cin >> n;
    for (i = 1; i <= 2*n; i++)
    {
        for (j = 1; j <= 2 * n; j++)
        {
            if (i <= n && ((j <= i) || (j >= 2 * n - i + 1)))
            {
                cout << " *";
            }
            else if (i > n && (j <= 2 * n - i + 1 || j >= i))
            {
                cout << " *";
            }
            else
            {
                cout << "  ";
            }
        }
        cout << endl;
    }
}

int main()
{

    // hollowRectangle();
    // invertedPyramid();
    // halfPyramidRight();
    // numberPyramid();
    // floydTriangle();
    butterfly();
    return 0;
}
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
  double pi = 3.14159;
  double raio, area;

  cin >> raio;

  area = pi * pow(raio, 2);

  cout << fixed << setprecision(4);

  cout << "A= " << area << endl;

  return 0;
}

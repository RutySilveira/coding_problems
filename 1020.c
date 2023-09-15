#include <stdio.h>

int main()
{

  int n;

  scanf("%d", &n);

  int anos = n / 365;
  int resto = n % 365;
  int meses = resto / 30;
  int dias = resto % 30;

  printf("%d ano(s)\n", anos);
  printf("%d mes(es)\n", meses);
  printf("%d dia(s)\n", dias);

  return 0;
}
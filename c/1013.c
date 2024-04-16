#include <stdio.h>
#include <stdlib.h>

int main()
{
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);

  int maior_ab = (a + b + abs(a - b)) / 2;

  int maior;

  if (maior_ab >= c)
  {
    maior = maior_ab;
  }
  else
  {
    maior = c;
  }

  printf("%d eh o maior\n", maior);

  return 0;
}

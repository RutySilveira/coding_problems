#include <stdio.h>

int main()
{
  int a, par = 0, impar = 0, positivo = 0, negativo = 0;

  for (int i = 0; i < 5; i++)
  {
    scanf("%d", &a);

    if (a % 2 == 0)
    {
      par += 1;
    }
    else
    {
      impar += 1;
    }

    if (a > 0)
    {
      positivo += 1;
    }
    else if (a < 0)
    {
      negativo += 1;
    }
  }

  printf("%d valor(es) par(es)\n", par);
  printf("%d valor(es) impar(es)\n", impar);
  printf("%d valor(es) positivo(s)\n", positivo);
  printf("%d valor(es) negativo(s)\n", negativo);

  return 0;
}

#include <stdio.h>
#include <stdlib.h>

int main()
{
  int cont, positivo;
  double n, soma;

  soma = 0;
  cont = 0;
  positivo = 0;

  while (cont < 6)
  {
    scanf("%lf", &n);
    if (n > 0)
    {
      positivo = positivo + 1;
      soma = soma + n;
    }

    cont = cont + 1;
  }

  if (positivo > 0)
  {
    double media = soma / positivo;
    printf("%d valores positivos\n", positivo);
    printf("%.1lf\n", media);
  }

  return 0;
}

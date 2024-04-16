#include <stdio.h>

int main()
{

  int a, contador, resultado;
  contador = 0;
  scanf("%d", &a);

  while (contador <= 9)
  {
    contador += 1;
    resultado = contador * a;
    printf("%d x %d = %d\n", contador, a, resultado);
  }

  return 0;
}
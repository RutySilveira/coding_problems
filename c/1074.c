#include <stdio.h>

int main()
{
  int a, b;
  scanf("%d", &a);

  for (int i = 0; i < a; i++)
  {
    scanf("%d", &b);
    char resultado[20] = "";

    if (b == 0)
    {
      sprintf(resultado, "NULL");
    }
    else
    {
      if (b % 2 == 0)
      {
        sprintf(resultado, "EVEN");
      }
      else
      {
        sprintf(resultado, "ODD");
      }

      if (b > 0)
      {
        sprintf(resultado, "%s POSITIVE", resultado);
      }
      else if (b < 0)
      {
        sprintf(resultado, "%s NEGATIVE", resultado);
      }
    }

    printf("%s\n", resultado);
  }

  return 0;
}

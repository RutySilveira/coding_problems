#include <stdio.h>

int main()
{
  int a, b;
  scanf("%d"
        "%d",
        &a, &b);

  float cachorroq = (b * 4.00);
  float x_salada = (b * 4.50);
  float x_bacon = (b * 5.00);
  float torrada = (b * 2.00);
  float refri = (b * 1.50);

  if (a == 1)
  {
    printf("Total: R$ %.2f\n", cachorroq);
  }
  else
  {
    if (a == 2)
    {
      printf("Total: R$ %.2f\n", x_salada);
    }
    else
    {
      if (a == 3)
      {
        printf("Total: R$ %.2f\n", x_bacon);
      }
      else
      {
        if (a == 4)
        {
          printf("Total: R$ %.2f\n", torrada);
        }
        else
        {
          if (a == 5)
          {
            printf("Total: R$ %.2f\n", refri);
          }
        }
      }
    }
  }
  return 0;
}
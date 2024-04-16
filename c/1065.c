#include <stdio.h>

int main()
{
  int a;
  scanf("%d", &a);

  if (a % 2 == 0)
  {
    a = a + 1;
  }

  for (int i = 0; i < 6; i++)
  {
    printf("%d\n", a);
    a += 2;
  }
  return 0;
}

#include <stdio.h>

int main()
{
  float nota1, nota2, nota3, nota4;
  float media, nota_exame, nova_media;
  int aluno_em_exame = 1;

  scanf("%f %f %f %f", &nota1, &nota2, &nota3, &nota4);

  media = (2 * nota1 + 3 * nota2 + 4 * nota3 + 1 * nota4) / 10;

  printf("Media: %.1f\n", media);
  if (media >= 7.0)
  {
    printf("Aluno aprovado.\n");
  }
  if (media < 5.0)
  {
    printf("Aluno reprovado.\n");
  }
  if (media >= 5.0 && media <= 6.9 && aluno_em_exame)
  {
    printf("Aluno em exame.\n");
    scanf("%f", &nota_exame);
    printf("Nota do exame: %.1f\n", nota_exame);
    nova_media = (nota_exame + media) / 2;
    if (nova_media >= 5.0)
    {
      printf("Aluno aprovado.\n");
    }
    if (nova_media <= 4.9)
    {
      printf("Aluno reprovado.\n");
    }
    printf("Media final: %.1f\n", nova_media);
  }

  return 0;
}

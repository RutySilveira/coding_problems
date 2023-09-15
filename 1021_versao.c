#include <stdio.h>
#include <math.h>

int main()
{
  float valor;
  scanf("%f", &valor);
  int notas[6] = {100, 50, 20, 10, 5, 2};

  printf("NOTAS:\n");

  for (int i = 0; i < 6; i++)
  {
    int nota = notas[i];
    int qtd = valor / nota;
    printf("%d nota(s) de R$ %d.00\n", qtd, nota);
    valor = fmod(valor, nota);
  }

  int valor_moeda = round(valor * 100);
  int moedas[6] = {100, 50, 25, 10, 5, 1};

  printf("MOEDAS:\n");

  for (int i = 0; i < 6; i++)
  {
    int moeda = moedas[i];
    float moeda_f = (float)moeda / 100;
    int qtd = valor_moeda / moeda;
    printf("%d moeda(s) de R$ %.2f\n", qtd, moeda_f);
    valor_moeda = fmod(valor_moeda, moeda);
  }

  return 0;
}
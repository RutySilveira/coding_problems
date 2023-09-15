#include <stdio.h>
#include <math.h>

int main()
{
  float valor;

  scanf("%f", &valor);

  int cem = valor / 100;
  valor = fmod(valor, 100);
  int cinquenta = valor / 50;
  valor = fmod(valor, 50);
  int vinte = valor / 20;
  valor = fmod(valor, 20);
  int dez = valor / 10;
  valor = fmod(valor, 10);
  int cinco = valor / 5;
  valor = fmod(valor, 5);
  int dois = valor / 2;
  valor = fmod(valor, 2);
  int um = valor / 1;
  valor = fmod(valor, 1);

  int valor_moeda = round(valor * 100);

  int cent_cinquenta = valor_moeda / 50;
  valor_moeda = valor_moeda % 50;
  int cent_vinte_e_cinco = valor_moeda / 25;
  valor_moeda = valor_moeda % 25;
  int cent_dez = valor_moeda / 10;
  valor_moeda = valor_moeda % 10;
  int cent_cinco = valor_moeda / 5;
  valor_moeda = valor_moeda % 5;
  int cent_um = valor_moeda / 1;

  printf("NOTAS:\n");
  printf("%d nota(s) de R$ 100.00\n", cem);
  printf("%d nota(s) de R$ 50.00\n", cinquenta);
  printf("%d nota(s) de R$ 20.00\n", vinte);
  printf("%d nota(s) de R$ 10.00\n", dez);
  printf("%d nota(s) de R$ 5.00\n", cinco);
  printf("%d nota(s) de R$ 2.00\n", dois);
  printf("MOEDAS:\n");
  printf("%d moeda(s) de R$ 1.00\n", um);
  printf("%d moeda(s) de R$ 0.50\n", cent_cinquenta);
  printf("%d moeda(s) de R$ 0.25\n", cent_vinte_e_cinco);
  printf("%d moeda(s) de R$ 0.10\n", cent_dez);
  printf("%d moeda(s) de R$ 0.05\n", cent_cinco);
  printf("%d moeda(s) de R$ 0.01\n", cent_um);

  return 0;
}
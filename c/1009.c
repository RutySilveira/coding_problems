#include <stdio.h>
 
int main() {
    char nome[15];
    double salario_fixo, total_vendas, salario_final;

    scanf("%s", nome);
    scanf("%lf", &salario_fixo);
    scanf("%lf", &total_vendas);

    salario_final = ((total_vendas * 15) / 100) + salario_fixo ;
    printf("TOTAL = R$ %.2lf\n", salario_final);
  
    return 0;
}
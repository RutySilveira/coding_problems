#include <stdio.h>

int main() {

    int codigo1, num_pecas1, codigo2, num_pecas2;
    float valor_peca1, valor_peca2, calculo;

    scanf("%d %d %f", &codigo1, &num_pecas1, &valor_peca1);
    scanf("%d %d %f", &codigo2, &num_pecas2, &valor_peca2);

    calculo = (num_pecas1 * valor_peca1) + (num_pecas2 * valor_peca2);
   
    printf("VALOR A PAGAR: R$ %.2f\n", calculo);
  
    return 0;
}
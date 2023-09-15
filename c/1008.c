#include <stdio.h>
 
int main() {
 
    int num_f, hrs_trab;
    float valor_h, salario;

    scanf("%d", &num_f);
    scanf("%d", &hrs_trab);
    scanf("%f", &valor_h);

    salario = hrs_trab * valor_h;
    printf("NUMBER = %d\n", num_f);
    printf("SALARY = U$ %.2f\n", salario);

    return 0;
}
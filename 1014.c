#include <stdio.h>

int main() {
  
    int km;
    float combustivel, consumo_m;
  
    scanf("%d", &km);
    scanf("%f", &combustivel);

    consumo_m = km / combustivel;
  
    printf("%.3f km/l\n", consumo_m);
  
    return 0;
}
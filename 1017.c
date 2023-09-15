#include <stdio.h>

int main() {
  
    int tempo_gasto, veloc_media;
    float quant_litros;
   
    scanf("%d", &tempo_gasto);
    scanf("%d", &veloc_media);

    quant_litros = (veloc_media * tempo_gasto) / 12.0;
  
    printf("%.3f\n", quant_litros);
  
    return 0;
}
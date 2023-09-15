#include <stdio.h>

int main() {

    int segundos_total, horas, resto, minutos, segundos;
    
    scanf("%d", &segundos_total);
 
    horas = segundos_total / 3600;
    resto = segundos_total % 3600;
    minutos = resto / 60;
    resto = resto % 60;
    segundos = resto;

    printf("%d:%d:%d\n", horas, minutos, segundos);
   
    return 0;
}
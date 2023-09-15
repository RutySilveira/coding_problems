#include <stdio.h>
#define PI 3.14159

int main() {

    double a1, b1, c1;
    float triangulo, circulo, trapezio, quadrado, retangulo;
   
    scanf("%lf %lf %lf", &a1, &b1, &c1);
    
    triangulo = (a1 * c1) / 2;
    circulo = PI * pow(c1, 2);
    trapezio = ((a1 + b1) * c1) / 2;
    quadrado = b1 * b1;
    retangulo = a1 * b1;
   
    printf("TRIANGULO: %.3f\n", triangulo);
    printf("CIRCULO: %.3f\n", circulo);
    printf("TRAPEZIO: %.3f\n", trapezio);
    printf("QUADRADO: %.3f\n", quadrado);
    printf("RETANGULO: %.3f\n", retangulo);
  
    return 0;
}
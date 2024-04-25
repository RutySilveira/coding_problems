import java.util.Locale;
import java.util.Scanner;

public class Area {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in).useLocale(Locale.US);

    double a, b, c, triangulo, circulo, trapezio, quadrado, retangulo;

    a = sc.nextDouble();
    b = sc.nextDouble();
    c = sc.nextDouble();

    triangulo = ((1.0 / 2.0) * a * c);
    circulo = 3.14159 * (c * c);
    trapezio = (1.0 / 2.0 * (a + b) * c);
    quadrado = b * b;
    retangulo = a * b;

    System.out.printf("TRIANGULO: %.3f%n", triangulo);
    System.out.printf("CIRCULO: %.3f%n", circulo);
    System.out.printf("TRAPEZIO: %.3f%n", trapezio);
    System.out.printf("QUADRADO: %.3f%n", quadrado);
    System.out.printf("RETANGULO: %.3f%n", retangulo);

    sc.close();
  }
}

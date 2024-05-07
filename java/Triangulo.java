import java.util.Scanner;
import java.util.Locale;

public class Triangulo {
  public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    Scanner sc = new Scanner(System.in);

    double area, perimetro;
    double a = sc.nextDouble();
    double b = sc.nextDouble();
    double c = sc.nextDouble();

    double somaLados1 = a + b;
    double somaLados2 = c + a;
    double somaLados3 = c + b;
    area = ((a + b) * c) / 2;
    perimetro = a + b + c;

    if (somaLados1 > c && somaLados2 > b && somaLados3 > a) {
      System.out.printf("Perimetro = %.1f%n", perimetro);
    } else {
      System.out.printf("Area = %.1f%n", area);
    }

    sc.close();
  }
}

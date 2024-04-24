import java.util.Locale;
import java.util.Scanner;

public class Esfera {

  public static void main(String[] args) {

    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in).useLocale(Locale.US);

    int raio;
    double volume, calculo;

    raio = sc.nextInt();

    calculo = Math.pow(raio, 3);
    volume = (4.0 / 3.0) * 3.14159 * calculo;

    System.out.printf("VOLUME = %.3f%n", volume);

    sc.close();
  }
}

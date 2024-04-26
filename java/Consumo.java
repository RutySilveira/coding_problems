import java.util.Locale;
import java.util.Scanner;

public class Consumo {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in).useLocale(Locale.US);

    int x;
    double y, distancia;

    x = sc.nextInt();
    y = sc.nextDouble();

    distancia = x / y;

    System.out.printf("%.3f km/l%n", distancia);

    sc.close();
  }
}

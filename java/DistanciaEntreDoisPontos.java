import java.util.Locale;
import java.util.Scanner;

public class DistanciaEntreDoisPontos {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in).useLocale(Locale.US);

    double x1, x2, y1, y2, p1, p2, distancia;

    x1 = sc.nextFloat();
    y1 = sc.nextFloat();
    x2 = sc.nextFloat();
    y2 = sc.nextFloat();

    p1 = Math.pow(x2 - x1, 2);
    p2 = Math.pow(y2 - y1, 2);

    distancia = Math.sqrt(p1 + p2);

    System.out.printf("%.4f%n", distancia);

    sc.close();
  }
}

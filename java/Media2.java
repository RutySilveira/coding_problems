import java.util.Scanner;
import java.util.Locale;

public class Media2 {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in).useLocale(Locale.US);
    double a, b, c, media;

    a = sc.nextDouble();
    b = sc.nextDouble();
    c = sc.nextDouble();

    media = ((a * 2) + (b * 3) + (c * 5)) / 10;

    System.out.printf("MEDIA = %.1f%n", media);

    sc.close();
  }
}

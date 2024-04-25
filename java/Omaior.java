import java.util.Locale;
import java.util.Scanner;

public class Omaior {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in).useLocale(Locale.US);

    int a, b, c, maiorab, maiorfinal;

    a = sc.nextInt();
    b = sc.nextInt();
    c = sc.nextInt();

    maiorab = (a + b + Math.abs(a - b)) / 2;
    maiorfinal = (maiorab + c + Math.abs(maiorab - c)) / 2;

    System.out.println(maiorfinal + " eh o maior");

    sc.close();

  }
}

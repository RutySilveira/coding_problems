import java.util.Locale;
import java.util.Scanner;

public class Diferenca {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in).useLocale(Locale.US);

    int a, b, c, d, calculo_diferenca;

    a = sc.nextInt();
    b = sc.nextInt();
    c = sc.nextInt();
    d = sc.nextInt();

    calculo_diferenca = (a * b) - (c * d);

    System.out.println("DIFERENCA = " + calculo_diferenca);

    sc.close();
  }
}

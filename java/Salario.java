import java.util.Locale;
import java.util.Scanner;

public class Salario {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in).useLocale(Locale.US);

    int n, hrs;
    double valor_hora, salario;

    n = sc.nextInt();
    hrs = sc.nextInt();
    valor_hora = sc.nextDouble();

    salario = hrs * valor_hora;

    System.out.println("NUMBER = " + n);
    System.out.printf("SALARY = U$ %.2f%n", salario);

    sc.close();
  }
}

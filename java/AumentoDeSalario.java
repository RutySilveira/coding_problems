import java.util.Scanner;
import java.util.Locale;

public class AumentoDeSalario {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    Scanner sc = new Scanner(System.in);

    double salariofinal, reajuste;
    double salario = sc.nextDouble();

    if (salario >= 0 && salario <= 400.00) {
      salariofinal = salario * 1.15;
      reajuste = salariofinal - salario;
      System.out.printf("Novo salario: %.2f%n", salariofinal);
      System.out.printf("Reajuste ganho: %.2f%n", reajuste);
      System.out.println("Em percentual: 15 %");
    } else if (salario >= 400.01 && salario <= 800.00) {
      salariofinal = salario * 1.12;
      reajuste = salariofinal - salario;
      System.out.printf("Novo salario: %.2f%n", salariofinal);
      System.out.printf("Reajuste ganho: %.2f%n", reajuste);
      System.out.println("Em percentual: 12 %");
    } else if (salario >= 800.01 && salario <= 1200.00) {
      salariofinal = salario * 1.10;
      reajuste = salariofinal - salario;
      System.out.printf("Novo salario: %.2f%n", salariofinal);
      System.out.printf("Reajuste ganho: %.2f%n", reajuste);
      System.out.println("Em percentual: 10 %");
    } else if (salario >= 1200.01 && salario <= 2000.00) {
      salariofinal = salario * 1.07;
      reajuste = salariofinal - salario;
      System.out.printf("Novo salario: %.2f%n", salariofinal);
      System.out.printf("Reajuste ganho: %.2f%n", reajuste);
      System.out.println("Em percentual: 7 %");
    } else {
      salariofinal = salario * 1.04;
      reajuste = salariofinal - salario;
      System.out.printf("Novo salario: %.2f%n", salariofinal);
      System.out.printf("Reajuste ganho: %.2f%n", reajuste);
      System.out.println("Em percentual: 4 %");
    }

    sc.close();
  }
}

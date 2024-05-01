import java.util.Scanner;
import java.util.Locale;

public class ImpostoDeRenda {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in);

    double salario = sc.nextDouble();
    double valorAt = salario - 2000;
    double valorFinal;

    if (valorAt <= 0) {
      System.out.println("Isento");
    } else if (valorAt <= 1000) {
      valorFinal = valorAt * 0.08;
      System.out.printf("R$ %.2f%n", valorFinal);
    } else if (valorAt <= 2500) {
      valorFinal = ((valorAt - 1000) * 0.18 + 80);
      System.out.printf("R$ %.2f%n", valorFinal);
    } else {
      valorFinal = ((valorAt - 2500) * 0.28 + 350);
      System.out.printf("R$ %.2f%n", valorFinal);
    }

    sc.close();
  }
}

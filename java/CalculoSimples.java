import java.util.Locale;
import java.util.Scanner;

public class CalculoSimples {

  public static void main(String[] args) {

    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in).useLocale(Locale.US);

    int cod1, n_pecas1, cod2, n_pecas2;
    double valor_peca1, valor_peca2, valor_a_pagar;

    cod1 = sc.nextInt();
    n_pecas1 = sc.nextInt();
    valor_peca1 = sc.nextDouble();

    cod2 = sc.nextInt();
    n_pecas2 = sc.nextInt();
    valor_peca2 = sc.nextDouble();

    valor_a_pagar = (n_pecas1 * valor_peca1) + (n_pecas2 * valor_peca2);

    System.out.printf("VALOR A PAGAR: R$ %.2f%n", valor_a_pagar);

    sc.close();
  }
}

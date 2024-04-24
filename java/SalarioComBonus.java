import java.util.Locale;
import java.util.Scanner;

public class SalarioComBonus {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in).useLocale(Locale.US);

    double salario_fixo, total_vendas, salario_final;

    String nome = sc.next();
    salario_fixo = sc.nextDouble();
    total_vendas = sc.nextDouble();

    salario_final = ((15 * total_vendas) / 100) + salario_fixo;

    System.out.printf("TOTAL= R$ %.2f%n", salario_final);

    sc.close();
  }
}

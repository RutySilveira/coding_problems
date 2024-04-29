import java.util.Scanner;
import java.util.Locale;

public class Lanche {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in).useLocale(Locale.US);

    double cachorroQuente = 4.00;
    double xSalada = 4.50;
    double xBacon = 5.00;
    double torradaSimples = 2.00;
    double refrigerante = 1.50;

    int codigo = sc.nextInt();
    int quantidade = sc.nextInt();
    double total;

    switch (codigo) {
      case 1:
        total = quantidade * cachorroQuente;
        System.out.printf("Total: R$ %.2f%n", total);
        break;
      case 2:
        total = quantidade * xSalada;
        System.out.printf("Total: R$ %.2f%n", total);
        break;
      case 3:
        total = quantidade * xBacon;
        System.out.printf("Total: R$ %.2f%n", total);
        break;
      case 4:
        total = quantidade * torradaSimples;
        System.out.printf("Total: R$ %.2f%n", total);
        break;
      case 5:
        total = quantidade * refrigerante;
        System.out.printf("Total: R$ %.2f%n", total);
        break;
      default:
        break;
    }
    sc.close();
  }
}

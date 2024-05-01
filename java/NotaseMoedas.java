import java.util.Locale;
import java.util.Scanner;

public class NotaseMoedas {

  public static void main(String[] args) {

    Locale.setDefault(Locale.US);

    Scanner sc = new Scanner(System.in).useLocale(Locale.US);

    float n;
    int cem, cinquenta, vinte, dez, cinco, dois, moedaum;
    int moedacinquenta, moedavintecinco, moedadez, moedacinco, moedaumcentavo;

    n = sc.nextFloat();

    cem = (int) (n / 100);
    n = n % 100;
    cinquenta = (int) (n / 50);
    n = n % 50;
    vinte = (int) (n / 20);
    n = n % 20;
    dez = (int) (n / 10);
    n = n % 10;
    cinco = (int) (n / 5);
    n = n % 5;
    dois = (int) (n / 2);
    n = n % 2;

    moedaum = (int) (n / 1);
    n = n % 1;
    n = Math.round(n * 100);
    moedacinquenta = (int) (n / 50);
    n = n % 50;
    moedavintecinco = (int) (n / 25);
    n = n % 25;
    moedadez = (int) (n / 10);
    n = n % 10;
    moedacinco = (int) (n / 5);
    moedaumcentavo = (int) (n % 5);

    System.out.println("NOTAS:");
    System.out.printf("%d nota(s) de R$ 100.00%n", cem);
    System.out.printf("%d nota(s) de R$ 50.00%n", cinquenta);
    System.out.printf("%d nota(s) de R$ 20.00%n", vinte);
    System.out.printf("%d nota(s) de R$ 10.00%n", dez);
    System.out.printf("%d nota(s) de R$ 5.00%n", cinco);
    System.out.printf("%d nota(s) de R$ 2.00%n", dois);
    System.out.println("MOEDAS:");
    System.out.printf("%d moeda(s) de R$ 1.00%n", moedaum);
    System.out.printf("%d moeda(s) de R$ 0.50%n", moedacinquenta);
    System.out.printf("%d moeda(s) de R$ 0.25%n", moedavintecinco);
    System.out.printf("%d moeda(s) de R$ 0.10%n", moedadez);
    System.out.printf("%d moeda(s) de R$ 0.05%n", moedacinco);
    System.out.printf("%d moeda(s) de R$ 0.01%n", moedaumcentavo);

    sc.close();
  }
}

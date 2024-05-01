import java.util.Scanner;

public class Cedulas {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int n, cem, cinquenta, vinte, dez, cinco, dois, um, resto;

    n = sc.nextInt();

    cem = n / 100;
    resto = n % 100;
    cinquenta = resto / 50;
    resto = resto % 50;
    vinte = resto / 20;
    resto = resto % 20;
    dez = resto / 10;
    resto = resto % 10;
    cinco = resto / 5;
    resto = resto % 5;
    dois = resto / 2;
    um = resto % 2;

    System.out.println(n);
    System.out.printf("%d nota(s) de R$ 100,00%n", cem);
    System.out.printf("%d nota(s) de R$ 50,00%n", cinquenta);
    System.out.printf("%d nota(s) de R$ 20,00%n", vinte);
    System.out.printf("%d nota(s) de R$ 10,00%n", dez);
    System.out.printf("%d nota(s) de R$ 5,00%n", cinco);
    System.out.printf("%d nota(s) de R$ 2,00%n", dois);
    System.out.printf("%d nota(s) de R$ 1,00%n", um);

    sc.close();
  }
}

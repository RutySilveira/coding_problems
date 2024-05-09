import java.util.Scanner;

public class SortSimples {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int menor = 0, meio = 0, maior = 0;

    int a = sc.nextInt();
    int b = sc.nextInt();
    int c = sc.nextInt();

    if (a <= b && a <= c) {
      menor = a;
      if (b <= c) {
        meio = b;
        maior = c;
      } else {
        meio = c;
        maior = b;
      }
    } else if (b <= a && b <= c) {
      menor = b;
      if (a <= c) {
        meio = a;
        maior = c;
      } else {
        meio = c;
        maior = a;
      }
    } else {
      menor = c;
      if (a <= b) {
        meio = a;
        maior = b;
      } else {
        meio = b;
        maior = a;
      }
    }

    System.out.printf("%d%n%d%n%d%n", menor, meio, maior);
    System.out.println();
    System.out.printf("%d%n%d%n%d%n", a, b, c);

    sc.close();
  }
}

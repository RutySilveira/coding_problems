import java.util.Scanner;

public class TesteDeSelecao1 {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int a = sc.nextInt();
    int b = sc.nextInt();
    int c = sc.nextInt();
    int d = sc.nextInt();

    int soma1 = a + b;
    int soma2 = c + d;

    if (b > c && d > a && soma2 > soma1 && c > 0 && d > 0 && a % 2 == 0) {
      System.out.println("Valores aceitos");
    } else {
      System.out.println("Valores nao aceitos");
    }

    sc.close();
  }
}

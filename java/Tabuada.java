import java.util.Scanner;

public class Tabuada {
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int produto;

    for (int i = 1; i <= 10; i++) {
      produto = i * n;
      System.out.printf("%d x %d = %d%n", i, n, produto);
    }

    sc.close();
  }
}

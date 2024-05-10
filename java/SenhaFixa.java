import java.util.Scanner;

public class SenhaFixa {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int x = 2002;

    while (n != x) {
      System.out.println("Senha Invalida");
      n = sc.nextInt();
    }

    System.out.println("Acesso Permitido");

    sc.close();
  }
}

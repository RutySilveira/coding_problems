import java.util.Scanner;

public class ParOuImpar {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int teste = sc.nextInt();

    for (int i = 0; i < teste; i++) {
      int n = sc.nextInt();
      String resultado = "";

      if (n == 0) {
        resultado = "NULL";
      } else if (n % 2 == 0) {
        resultado = "EVEN";
        {
        }
      } else {
        resultado = "ODD";
      }
      if (n > 0) {
        resultado += " POSITIVE";
      } else if (n < 0) {
        resultado += " NEGATIVE";
      }
      System.out.println(resultado);
    }

    sc.close();
  }
}

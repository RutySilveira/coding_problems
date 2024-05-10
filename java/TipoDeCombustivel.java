import java.util.Scanner;

public class TipoDeCombustivel {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int alcool = 0;
    int gasolina = 0;
    int diesel = 0;
    int n = sc.nextInt();

    while (n != 4) {
      if (n == 1) {
        alcool = alcool + 1;
      }
      if (n == 2) {
        gasolina = gasolina + 1;
      }
      if (n == 3) {
        diesel = diesel + 1;
      }
      n = sc.nextInt();
    }

    System.out.println("MUITO OBRIGADO");
    System.out.printf("Alcool: %d%nGasolina: %d%nDiesel: %d%n", alcool, gasolina, diesel);

    sc.close();
  }
}

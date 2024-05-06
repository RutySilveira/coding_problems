import java.util.Scanner;

public class TempoDeJogo {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int d;
    int a = sc.nextInt();
    int b = sc.nextInt();

    int duracao = (24 - a + b) % 24;

    if (duracao == 0) {
      d = 24;
    } else {
      d = duracao;
    }

    System.out.printf("O JOGO DUROU %d HORA(S)%n", d);

    sc.close();
  }
}

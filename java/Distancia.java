
import java.util.Scanner;

public class Distancia {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int distancia, minutos;

    distancia = sc.nextInt();

    minutos = 2 * distancia;

    System.out.printf("%d minutos", minutos);

    sc.close();
  }
}

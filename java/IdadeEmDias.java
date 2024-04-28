import java.util.Scanner;

public class IdadeEmDias {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int idadeDias, anos, meses, dias, resto_anos;

    idadeDias = sc.nextInt();

    anos = idadeDias / 365;
    resto_anos = idadeDias % 365;
    meses = resto_anos / 30;
    dias = resto_anos % 30;

    System.out.printf("%d ano(s)%n", anos);
    System.out.printf("%d mes(es)%n", meses);
    System.out.printf("%d dia(s)%n", dias);

    sc.close();
  }
}

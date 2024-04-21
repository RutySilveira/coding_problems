import java.util.Scanner;

// java -ea ExtremamenteBasico.java
public class ExtremamenteBasico {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int a = sc.nextInt();
    int b = sc.nextInt();
    int x = a + b;

    System.out.println("X = " + x);

    sc.close();
  }
}

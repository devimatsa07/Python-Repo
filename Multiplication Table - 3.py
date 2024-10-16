import java.util.Scanner;
public class MultiplicationTable {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int N = scanner.nextInt();
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        
        for (int i = A; i <= B; i++) 
        {
            System.out.println(N+" x "+i+" = "+(N * i));
        }
        scanner.close();
    }
}

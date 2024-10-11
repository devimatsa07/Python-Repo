import java.util.Scanner;
public class ExponentialOrQuadratic 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        if (Math.pow(2, n) > Math.pow(n, 2)) 
        {
            System.out.println("Yes");
        } 
        else 
        {
            System.out.println("No");
        }
    }
}

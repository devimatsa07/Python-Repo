import java.util.Scanner;
public class CarChoice 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        while (t-- > 0) {
            int x1 = scanner.nextInt();
            int x2 = scanner.nextInt();
            int y1 = scanner.nextInt();
            int y2 = scanner.nextInt();
            double cost1 = (double) y1 / x1;
            double cost2 = (double) y2 / x2;
            if (cost1 < cost2) 
            {
                System.out.println("-1");
            } 
            else if (cost1 == cost2) 
            {
                System.out.println("0");
            } 
            else 
            {
                System.out.println("1");
            }
        }
    }
}
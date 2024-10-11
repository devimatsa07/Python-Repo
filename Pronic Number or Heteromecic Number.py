import java.util.Scanner;
public class PronicNumber 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int i = 1;
        while (i * (i + 1) <= x) 
        {
            if (i * (i + 1) == x) 
            {
                System.out.println("YES");
                return;
            }
            i++;
        }
        System.out.println("NO");
    }
}

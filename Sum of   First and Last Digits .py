import java.util.Scanner;
public class Sum
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int lastDigit = number % 10;
        int originalNumber = number;
        while (number >= 10) 
        {
            number /= 10;
        }
        int sum = number + lastDigit;
        System.out.println(sum);
    }
}
import java.util.Scanner;
public class Neon
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int sum=0;
        int square=n*n;
        while(square!=0)
        {
            int r=square%10;
            sum=sum+r;
            square=square/10;
        }
        if(n==sum)
        {
            System.out.println("Neon Number");
        }
        else
        {
            System.out.println("Not Neon Number");
        }
    }
}
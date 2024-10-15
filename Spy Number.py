import java.util.Scanner;
public class Spy
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int num=sc.nextInt();
        int sum=0;
        int product=1;
        while(num>0)
        {
            int r=num%10;
            sum=sum+r;
            product=product*r;
            num/=10;
        }
        if(sum==product)
        {
            System.out.println("Spy Number");
        }
        else
        {
            System.out.println("Not Spy Number");
        }
    }
}
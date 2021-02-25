import java.util.*;
public class Solution

{
public static boolean isInside (double x, double y)  
{  
double distance = Math.sqrt((x * x) + (y * y));
return (distance < 1.0);
}

public static double calculatePI (int num)

{
Random random= new Random (System.currentTimeMillis());   
int repeats = 0;
double PI = 0;
for (int i = 1; i <= num; i++)

{
double x = (random.nextDouble()) * 2 - 1.0;
double y = (random.nextDouble()) * 2 - 1.0;
if (isInside(x, y))
{
repeats++;
  
}

}
double dRepeats = num;

PI = (4.0 * (repeats/dRepeats));

return PI;
}
  
public static void main (String[] args)
{
Scanner scan = new Scanner (System.in);
int num = scan.nextInt();
double PI = calculatePI(num);
System.out.println ("approximate value of PI = " + PI);   

}

}
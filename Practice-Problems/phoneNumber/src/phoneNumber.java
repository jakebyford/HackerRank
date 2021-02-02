
		import java.util.Scanner;

		public class phoneNumber {
		   public static void main(String[] args) {
		      Scanner scnr = new Scanner(System.in);
		      long phoneNumber;
		      // Add more variables as needed

		      phoneNumber = scnr.nextLong();
		      
		      System.out.print(" (" + (phoneNumber / 10000000) + ") ");
		      System.out.print((phoneNumber / 10000) % 10000 + "-");
		      System.out.println(phoneNumber % 10000);
		      /* Type your code here. */
		   }
		}

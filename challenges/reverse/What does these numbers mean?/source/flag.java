import java.util.Scanner;
import java.util.Random;
import java.io.IOException;
import java.util.Arrays;

class flag
{
	public static void main(String[] args){


		Scanner input = new Scanner(System.in);
    	
    		System.out.print("Key to get random parts of the flag: ");
    		String userin = input.next();

		String[] result = {"56, 56, 50, 98, 57, 49, 54, 48", "50, 50, 48, 54, 97, 99, 50, 57", "98, 56, 53, 51, 100, 50, 101, 97", "54, 49, 49, 52, 48, 56, 52, 50"};

		byte[] bytes = { 103, 114, 121, 112, 104, 111, 110, 115, 50, 48, 50, 48};

		String validate = new String(bytes);

		if(userin.equals(validate))
		{
			int i = (int)(4.0 * Math.random());
			System.out.println(i + ") Here is part of the Flag from within GCTF{}: ");
			System.out.println(result[i]);
		}
		else{
			System.out.println("Sorry the key is wrong, please try finding it via our social media");
		}
	}
}

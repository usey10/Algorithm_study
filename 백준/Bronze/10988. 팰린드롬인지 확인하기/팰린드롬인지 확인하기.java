import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		String word = scan.nextLine();
		
		int lenNum = word.length();
		int slice = lenNum/2;
		int result = 0;
		
		for(int i=0;i < slice;i++) {
			int temp = (word.charAt(i) == word.charAt(lenNum-1-i)) ? 0:1;
			result = temp + result;
		}

		System.out.println((result==0) ? 1 : 0);

	}
}
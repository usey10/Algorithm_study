import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		String S = scan.next();
		int i = scan.nextInt();
		
		System.out.println(S.charAt(i-1));
	}
}
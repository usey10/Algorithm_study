import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		String A = scan.next();
		String B = scan.next();
		
		int result = Integer.parseInt(A) * Integer.parseInt(B);
		System.out.println(result);
	}
}
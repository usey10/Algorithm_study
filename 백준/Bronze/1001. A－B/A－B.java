import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		String[] lines = scanner.nextLine().split("\\s+");
		
		int A = Integer.parseInt(lines[0]);
		int B = Integer.parseInt(lines[1]);
		
		System.out.println(A-B);
	}
}

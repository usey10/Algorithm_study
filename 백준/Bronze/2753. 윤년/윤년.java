import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String year = br.readLine();
		
		int y = Integer.parseInt(year);
		if ((y % 4) != 0) {
			System.out.println(0);
		} else if ((y%400)==0) {
			System.out.println(1);
		} else if ((y%100)==0) {
			System.out.println(0);
		} else {
			System.out.println(1);
		}
	}
}
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		int T = Integer.parseInt(line);
		
		for (int i=1;i<=T;i++) {
			String[] tcase = br.readLine().split(" ");
			int A = Integer.parseInt(tcase[0]);
			int B = Integer.parseInt(tcase[1]);
			System.out.println(A+B);
		}
				
	}
} 
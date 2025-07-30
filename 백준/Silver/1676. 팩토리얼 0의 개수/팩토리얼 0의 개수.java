import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class Main {


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int zero = 0;
		long sum = 1;
		
		
		for (int i=1;i<=N;i++) {
			sum *= i;
			while ((sum%10) == 0) {
				sum /= 10;
				sum %= 1000000000000L;
				zero++;
			}
			sum %= 1000000000000L;
			

		}
		
		System.out.println(zero);
		
		
	}
}

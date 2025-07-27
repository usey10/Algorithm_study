import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] lines = br.readLine().split(" ");
		
		int N = Integer.parseInt(lines[0]);
		int K = Integer.parseInt(lines[1]);
		
		int de = 1;
		int nu = 1;
		
		for(int i=K, j=N;i>0;i--) {
			de *= i;
			nu *= j;
			j--;
		}
		System.out.println(nu/de);
	}
}
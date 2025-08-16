import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		int[] dps = new int[n+1];
		dps[1] = 1;
		
			
		for (int i=2;i<=n;i++) {
			if (i == 2) dps[2] = 3;
			else dps[i] = (dps[i-1] + dps[i-2]*2)%10007;
		}
			
		System.out.println(dps[n]);
		
	}
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int X = Integer.parseInt(br.readLine());
		
		int[] memo = new int[1000001];
		memo[2] = 1;
		memo[3] = 1;
		
		System.out.println(dp(memo, X));
		
	}
	static int dp(int[] m, int x) {
		if (x == 1) return 0;
		else if (m[x] != 0) return m[x];
		
		int min = 0;
		if (x % 3 == 0 && x % 2 == 0) {
			min = Math.min(Math.min(dp(m,x/3), dp(m, x/2)), dp(m,x-1));
			m[x] = min + 1;
			return m[x];
		} else if (x % 3 == 0) {
			min = Math.min(dp(m,x/3), dp(m,x-1));
			m[x] = min + 1;
			return m[x];
		} else if (x % 2 == 0) {
			min = Math.min(dp(m,x/2), dp(m,x-1));
			m[x] = min + 1;
			return m[x];
		} else {
			m[x] = dp(m, x-1) + 1;
			return m[x];
		}
	}
}
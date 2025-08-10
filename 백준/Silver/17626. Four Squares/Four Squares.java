import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		// 제곱수 리스트
		int[] dp = new int[50001];
		
		for (int i=1;i<=Math.sqrt(n);i++) {
			dp[i*i] = 1;
		}
		
		for (int i=1;i<=n;i++) {
			if (dp[i] != 0) continue;
			else {
				int min = Integer.MAX_VALUE;
				for (int j=1;j<=Math.sqrt(i);j++) {
					min = Math.min(min, 1 + dp[i - j*j] );
				}
				dp[i] = min;
			}
		}

		
		System.out.println(dp[n]);	

	}
}

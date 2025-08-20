import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int[][] nset = new int[N][2];
		
		
		for (int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			nset[i][0] = Integer.parseInt(st.nextToken());
			nset[i][1] = Integer.parseInt(st.nextToken());
		}
		
		int[][] dp = new int[N+1][K+1];
		
		for (int i = 1;i<=N;i++) {
			int w = nset[i-1][0];
			int v = nset[i-1][1];
			int[] before = dp[i-1];
			int[] now = Arrays.copyOf(before, K+1);
			
//			System.out.println("w:"+ w + ", v: "+v);
			if (w > K) {
				dp[i] = now;
				continue;
			}
			
			// 추가 되었을 때 넣기
			for (int j = w+1 ;j<=K ;j++) {
				if (now[j-w] != 0) {
					now[j] = Math.max(before[j - w] + v, before[j]);
				}
			}
			
			now[w] = Math.max(before[w], v);
			dp[i] = now;
			
//			System.out.println(Arrays.deepToString(dp));
			
		}
		
		System.out.println(Arrays.stream(dp[N]).max().getAsInt());
	}

}

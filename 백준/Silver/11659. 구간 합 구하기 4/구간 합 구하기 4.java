import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] sums = new int[N+1];
		int sum = 0;
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		for (int i=1;i<=N;i++) {
			int x = Integer.parseInt(st2.nextToken());
			sum += x;
			sums[i] = sum;
		}
		
		// i번째~j번째 구하기
		for (int tc=0;tc<M;tc++) {
			String[] lines = br.readLine().split(" ");
			int i = Integer.parseInt(lines[0]);
			int j = Integer.parseInt(lines[1]);
			sb.append(sums[j] - sums[i-1]).append("\n");
		}
		
		System.out.println(sb);
		
	}

}
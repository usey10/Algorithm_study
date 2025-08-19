import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static long[] fib(int x, long[][] alls) {
		if (alls[x] == null) {
			long[] x1 = fib(x-1, alls);
			long[] x2 = fib(x-2, alls);
			alls[x] = new long[] {x1[0] + x2[0], x1[1] + x2[1]};
		}
		
		return alls[x];
		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc=0;tc<T;tc++) {
			
			int N = Integer.parseInt(br.readLine());
			long[][] alls = new long[N+1][];
			
			if (N >= 2) {
				alls[0] = new long[] {1, 0};
				alls[1] = new long[] {0, 1};
				
				long[] li = fib(N, alls);
				
				sb.append(li[0]).append(" ").append(li[1]).append("\n");
			
			} else if (N == 1){
				sb.append(0).append(" ").append(1).append("\n");
			
			} else {
				sb.append(1).append(" ").append(0).append("\n");
			}
			
		}
		
		System.out.println(sb.toString());
		

		
	}
}
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
		
		st = new StringTokenizer(br.readLine());
		long[] childs = new long[N];
		for (int i=0;i<N;i++) {
			childs[i] = Long.parseLong(st.nextToken());
		}
		
		long[] min = new long[N-1];
		for (int i=0;i<N-1;i++) {
			min[i] = childs[i+1] - childs[i];
		}
		
		Arrays.sort(min);
		
		long sum = 0;
		
		for (int i=0;i<N-K;i++) {
			sum += min[i];
		}
		
		System.out.println(sum);

		
	}
}
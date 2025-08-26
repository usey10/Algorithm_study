import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[][] meets = new int[N][2];
		
		StringTokenizer st;
		
		for (int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			meets[i][0] = s;
			meets[i][1] = e;
		}
		
		Arrays.sort(meets, (a,b) -> {
			if (a[1] != b[1]) {
				return a[1] - b[1];
			} else {
				return a[0] - b[0];
			}
		});
		
		int cnt = 0;
		int now = -1;
		for (int i=0;i<N;i++) {
			if (now <= meets[i][0]) {
				cnt++;
				now = meets[i][1];
			}
		}
		
		System.out.println(cnt);

		
	}
}
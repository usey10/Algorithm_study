import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int i=0;i<T;i++) {
			StringTokenizer stnm = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(stnm.nextToken());
			int M = Integer.parseInt(stnm.nextToken());
			
			Deque<int[]> deque = new ArrayDeque<>();
			int[] im = new int[N];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j=0;j<N;j++) {
				int check = Integer.parseInt(st.nextToken());
				int[] doc = {j, check};
				deque.add(doc);
				im[j] = check;
			}
			
			int cnt = 0;
			Arrays.sort(im);
			int importantCheck = N-1;
			while(true) {
				int[] pops = deque.removeFirst();
				if (pops[1] == im[importantCheck] && pops[0] == M) {
					cnt++;
					importantCheck--;
					break;
				} else if (pops[1] == im[importantCheck]) {
					cnt++;
					importantCheck--;
					continue;
				} else {
					deque.add(pops);
				}
			}
			sb.append(cnt).append("\n");
		}
		
		System.out.println(sb.toString());
	}
}

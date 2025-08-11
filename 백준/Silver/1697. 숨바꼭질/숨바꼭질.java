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
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());

		int[] nSet = new int[100001];
		boolean[] visited = new boolean[100001];
		
		
		Deque<int[]> deque = new ArrayDeque<>();
		int[] first = {n, 0};
		deque.add(first);
		
		visited[n] = true;
		while (!deque.isEmpty()) {
			int[] t = deque.poll();
			if (t[0] == k) break;
			
			if (t[0]-1 >= 0 && visited[t[0]-1] == false) {
				visited[t[0]-1] = true;
				nSet[t[0]-1] = t[1]+1;
				int[] tmp = {t[0]-1, t[1]+1};
				deque.add(tmp);
			}
			if (t[0]+1 <= 100000 && visited[t[0]+1] == false) {
				visited[t[0]+1] = true;
				nSet[t[0]+1] = t[1]+1;
				int[] tmp = {t[0]+1, t[1]+1};
				deque.add(tmp);
			}
			if (2*t[0] <= 100000 && visited[2*t[0]] == false) {
				visited[2*t[0]] = true;
				nSet[2*t[0]] = t[1]+1;
				int[] tmp = {2*t[0], t[1]+1};
				deque.add(tmp);
			}
			
		}
		
		
		System.out.println(nSet[k]);

	}
}

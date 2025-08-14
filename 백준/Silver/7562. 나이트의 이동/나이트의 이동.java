import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class Main{
	static boolean[][] visited;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc<T;tc++) {
			int N = Integer.parseInt(br.readLine());
			visited = new boolean[N][N];
			
			String[] lines1 = br.readLine().split(" ");
			String[] lines2 = br.readLine().split(" ");
			
			int[] start = new int[] { Integer.parseInt(lines1[0]), Integer.parseInt(lines1[1])};
			int[] end = new int[] { Integer.parseInt(lines2[0]), Integer.parseInt(lines2[1])};
			
			Deque<int[]> deque1 = new ArrayDeque<>();
			Deque<int[]> deque2 = new ArrayDeque<>();
			
			deque1.add(start);
			visited[start[0]][start[1]] = true;
			
			int result = bfs(deque1, deque2, end);
			
			System.out.println(result);
			
		}
		
		
	}
	static int bfs(Deque<int[]> d1, Deque<int[]> d2, int[] e) {
		int cnt = 0;
		while (!d1.isEmpty()) {
			int[] k = d1.poll();
			if (k[0] == e[0] && k[1] == e[1]) {
				return cnt;
			}
			
			int[] nx = {-2, -1, 1, 2, -2, -1, 1, 2};
			int[] ny = {-1, -2, -2, -1, 1, 2, 2, 1};
			for (int i=0;i<nx.length;i++) {
				int[] nk = {k[0]+nx[i], k[1]+ny[i]};
				if (nk[0] >= 0 && nk[0] < visited.length && nk[1] >= 0 && nk[1] < visited.length) {
					if (!visited[nk[0]][nk[1]]) {
						visited[nk[0]][nk[1]] = true;
						d2.add(nk);
					}
				}
			}
		}
//        for (int[] arr : d1) {
//            System.out.print(Arrays.toString(arr));
//        }
//        System.out.println();
//        for (int[] arr : d2) {
//        	System.out.print(Arrays.toString(arr));
//        }
//        System.out.println();
        
		if (d1.isEmpty() && d2.isEmpty()) return cnt;
		return bfs(d2,d1,e) + 1;
	}
}
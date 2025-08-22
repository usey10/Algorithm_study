import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static void bfs(boolean[][] land) {
		while (!xy.isEmpty()) {
			int[] xys = xy.poll();
			int[] dx = {-1, 1, 0, 0};
			int[] dy = {0, 0, -1, 1};
			
			for (int k=0;k<dx.length;k++) {
				int nx = xys[0] + dx[k];
				int ny = xys[1] + dy[k];
				if (nx >= 0 && nx < land.length && ny >= 0 && ny < land[0].length) {
					if (land[nx][ny]) {
						land[nx][ny] = false;
						xy.add(new int[] {nx, ny});
					}
				}
				
			}
		}
	}
	static Deque<int[]> xy;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		
		StringTokenizer st;
		
		for (int tc=0;tc<T;tc++) {
			st = new StringTokenizer(br.readLine());
			int M = Integer.parseInt(st.nextToken());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			
			boolean[][] land = new boolean[M][N];
			
			
			for (int i=0;i<K;i++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				land[x][y] = true;
			}
			
			xy = new ArrayDeque<>();
			int cnt = 0;
			
			for (int i=0;i<M;i++) {
				for (int j=0;j<N;j++) {
					if (land[i][j]) {
						cnt++;
						land[i][j] = false;
						xy.add(new int[] {i,j});
						bfs(land);
					}
				}
			}
			
			sb.append(cnt).append("\n");
		}
		
		System.out.println(sb.toString());
	}

}

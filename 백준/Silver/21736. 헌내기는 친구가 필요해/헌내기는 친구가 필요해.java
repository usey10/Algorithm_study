import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		char[][] campus = new char[N][M];
		
		int[] start = new int[2];
		
		for (int i=0;i<N;i++) {
			campus[i] = br.readLine().toCharArray();
			for (int j=0;j<M;j++) {
				if (campus[i][j] == 'I') {
					start[0] = i;
					start[1] = j;
				}
			}
		}
		
		// System.out.println(Arrays.deepToString(campus));
		
		boolean[][] visited = new boolean[N][M];
		Deque<int[]> deque = new ArrayDeque<>();
		
		deque.add(start);
		visited[start[0]][start[1]] = true;
		int cnt = 0;
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		
		while (!deque.isEmpty()) {
			int[] xy = deque.pollFirst();
			
			for (int i=0;i<dx.length;i++) {
				int newX = xy[0] + dx[i];
				int newY = xy[1] + dy[i];
				
				if (newX >= 0 && newY >= 0 && newX < N && newY < M && !visited[newX][newY] && campus[newX][newY] != 'X') {
					if (campus[newX][newY] == 'P') cnt++;
					
					visited[newX][newY] = true;
					deque.add(new int[] {newX, newY});
				}
			}
		}
		
		if (cnt != 0) System.out.println(cnt);
		else System.out.println("TT");
		
	}

}

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
		int m = Integer.parseInt(st.nextToken());
		
		// 미로 받기
		char[][] maze = new char[n][];
		
		for (int i=0;i<n;i++) {
			String lines = br.readLine();
			maze[i] = lines.toCharArray();
		}
		
		int[][] visited = new int[n][m];
		
		Deque<int[]> queue = new ArrayDeque<>();
		int[] xy = {0,0};
		queue.add(xy);
		visited[0][0] = 1;

		while (!queue.isEmpty()) {
			int[] xys = queue.pollFirst();
			// System.out.println(Arrays.toString(xys));
			int x = xys[0];
			int y = xys[1];
			
			int[][] exy = {{x-1, y}, {x+1, y}, {x, y-1}, {x,y+1}};
			
			for (int i = 0;i<exy.length;i++) {
				if (exy[i][0] >= 0 && exy[i][1] >= 0 && exy[i][0] <= n-1 && exy[i][1] <= m-1) {
					if (maze[exy[i][0]][exy[i][1]] == '1' && visited[exy[i][0]][exy[i][1]] == 0) {
						queue.addLast(exy[i]);
						visited[exy[i][0]][exy[i][1]] = visited[x][y] + 1;
					}
					else if (maze[exy[i][0]][exy[i][1]] == '1' && visited[exy[i][0]][exy[i][1]] != 0) {
						visited[exy[i][0]][exy[i][1]] = Math.min(visited[x][y] + 1, visited[exy[i][0]][exy[i][1]]);
					}
				}
			}
		}
		
		System.out.println(visited[n-1][m-1]);

	}
}

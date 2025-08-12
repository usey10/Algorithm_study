import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;
import java.util.StringTokenizer;

//- visited 배열 필요
//- dfs? for 문으로 돌면서 visited false 이고 1이면 stack 에 넣기
//- stack 에서 pop 하면서 visited 체크, 주변이 1이고 visited false 면 스택에 다시 넣기
//- while 문 한번 다 돌아갔으면 count 1 하기 식으로!

public class Main {
	static int dfs(int w, int h, String[][] map) {
		while (!deque.isEmpty()) {
			int[] xy = deque.pollLast();
			int[] dx = {-1, 0, 1, -1, 1, -1, 0, 1};
			int[] dy = {-1, -1, -1, 0, 0, 1, 1, 1};
			for (int i = 0;i<dx.length;i++) {
				int nx = xy[0] + dx[i];
				int ny = xy[1] + dy[i];
				if (nx >= 0 && nx < h && ny >= 0 && ny < w) {
					if (!visited[nx][ny] && map[nx][ny].equals("1")) {
						visited[nx][ny] = true;
						int[] nxy = {nx, ny};
						deque.add(nxy);
					}
				}
			}
		}
		return 1;
	}
	static boolean[][] visited = new boolean[50][50];
	static Deque<int[]> deque = new ArrayDeque<>();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		while (true) {
			visited = new boolean[50][50];
			deque = new ArrayDeque<>();
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int w = Integer.parseInt(st.nextToken());
			int h = Integer.parseInt(st.nextToken());
			
			if (w==0&& h==0) break;
			
			String[][] map = new String[h][];
			for (int i=0;i<h;i++) {
				map[i] = br.readLine().split(" ");
			}
			
			
			int cnt = 0;
			for (int i=0;i<h;i++) {
				for (int j=0;j<w;j++) {
					if (map[i][j].equals("1") && !visited[i][j]) {
						visited[i][j] = true;
						int[] xy = {i, j};
						deque.add(xy);
						cnt += dfs(w,h, map);
					}
				}
			}
			
			sb.append(cnt).append("\n");
			
			
		}
		
		System.out.println(sb.toString());
		
	}

}
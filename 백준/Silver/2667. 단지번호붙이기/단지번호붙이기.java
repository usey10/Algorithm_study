import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
	public static void dfs(char[][] lines, int x, int y, int groupNum) {
		
		if (x-1 >= 0 && lines[x-1][y] == '1') {
			if (visited[x-1][y] == false) {
				Hgroup.put(groupNum, (Hgroup.get(groupNum)+1));
				visited[x-1][y] = true;
				dfs(lines, x-1, y, groupNum);
			}
		}
		if (x+1 < lines.length && lines[x+1][y] == '1') {
			if (visited[x+1][y] == false) {
				Hgroup.put(groupNum, (Hgroup.get(groupNum)+1));
				visited[x+1][y] = true;
				dfs(lines, x+1, y, groupNum);
			}
		}
		if (y-1 >= 0 && lines[x][y-1] == '1') {
			if (visited[x][y-1] == false) {
				Hgroup.put(groupNum, (Hgroup.get(groupNum)+1));
				visited[x][y-1] = true;
				dfs(lines, x, y-1, groupNum);
			}
		}
		if (y+1 < lines.length && lines[x][y+1] == '1') {
			if (visited[x][y+1] == false) {
				Hgroup.put(groupNum, (Hgroup.get(groupNum)+1));
				visited[x][y+1] = true;
				dfs(lines, x, y+1, groupNum);
			}
		}
	}
	
	public static Map<Integer, Integer> Hgroup = new HashMap<>();
	public static boolean[][] visited;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		
		visited = new boolean[n][n];
		// 인접 받기
		char[][] lines = new char[n][];
		for (int i=0;i<n;i++) {
			lines[i] = br.readLine().toCharArray();
		}
		
		int groupNum = 1;
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				if (lines[i][j] == '1' && visited[i][j] == false) {
					visited[i][j] = true;
					Hgroup.put(groupNum, 1);
					dfs(lines, i, j, groupNum);
					groupNum += 1;
					}
				}
			}
		
		sb.append(Hgroup.size()).append("\n");
		
		int[] get = new int[Hgroup.size()];
		int idx = 0;
		for (int li : Hgroup.keySet()) {
			get[idx++] = Hgroup.get(li);
		}
		Arrays.sort(get);
		for (int li1:get) {
			sb.append(li1).append("\n");
		}
		
		System.out.println(sb);

	}
}

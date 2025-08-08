import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int v = Integer.parseInt(st.nextToken());
		
		// map
		Map<Integer, ArrayList<Integer>> tree = new HashMap<>();
		
		for (int i=0;i<M;i++) {
			String[] lines = br.readLine().split(" ");
			int x = Integer.parseInt(lines[0]);
			int y = Integer.parseInt(lines[1]);
			
			if (tree.containsKey(x)) {
				tree.get(x).add(y);
			} else {
				ArrayList<Integer> list = new ArrayList<>();
				list.add(y);
				tree.put(x, list);
			}
			
			if (tree.containsKey(y)) {
				tree.get(y).add(x);
			} else {
				ArrayList<Integer> list = new ArrayList<>();
				list.add(x);
				tree.put(y, list);
			}
			
		}
		
		// dfs
		Stack<Integer> dfs = new Stack<>();
		Stack<Integer> before = new Stack<>();
		
		// dfs 풀기
		dfs.add(v);
		
		boolean[] visited = new boolean[N+1];

		while (!dfs.isEmpty()) {
			int node = dfs.pop();
			if (visited[node] == false) {
				visited[node] = true;
				sb.append(node).append(" ");
				
				ArrayList<Integer> nList = tree.get(node);
				if (nList == null) {
					break;
				}
				Collections.sort(nList);
				
				for (int li:nList) {
					if (visited[li] == false) {
						before.push(node);
						dfs.push(node);
						dfs.push(li);
						break;
					}
				}
				
			} else {
				if (!before.isEmpty()) {
					before.pop();
					ArrayList<Integer> nList = tree.get(node);
					Collections.sort(nList);
					
					for (int li:nList) {
						if (visited[li] == false) {
							before.push(node);
							dfs.push(node);
							dfs.push(li);
							break;
						}
					}
				}
			}
			
		}
		sb.append("\n");
		
		
		// bfs
		Deque<Integer> bfs = new ArrayDeque<>();
		
		bfs.add(v);
		boolean[] visited2 = new boolean[N+1];
		
		while (!bfs.isEmpty()) {
			int node = bfs.removeFirst();
			if (visited2[node] == false) {
				visited2[node] = true;
				sb.append(node).append(" ");
				ArrayList<Integer> nList = tree.get(node);
				if (nList == null) {
					break;
				}
				for (int li: nList) {
					bfs.add(li);
				}
			} else {
				continue;
			}
		}

		System.out.println(sb);
		
	}

}
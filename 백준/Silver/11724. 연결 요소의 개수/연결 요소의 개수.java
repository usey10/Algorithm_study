import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		Map<Integer, ArrayList<Integer>> graph = new HashMap<>();
		int first = 0;
		for (int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int f = Integer.parseInt(st.nextToken());
			int l = Integer.parseInt(st.nextToken());
			
			
			if (graph.containsKey(f)) {
				graph.get(f).add(l);
			} else {
				ArrayList<Integer> li = new ArrayList<>();
				li.add(l);
				graph.put(f, li);
			}
			if (graph.containsKey(l)) {
				graph.get(l).add(f);
			} else {
				ArrayList<Integer> li = new ArrayList<>();
				li.add(f);
				graph.put(l, li);
			}
			if (i == 0) first = f;
		}
		
		boolean[] visited = new boolean[N+1];
		Deque<Integer> deque = new ArrayDeque<>();
		int cnt = 0;
		
		for (int k = 1;k<N+1;k++) {
			if (!visited[k]) {
				visited[k] = true;
				deque.add(k);
				cnt++;
			}
			
			while (!deque.isEmpty()) {
				int v = deque.poll();
				
				ArrayList<Integer> check = graph.get(v);
				if (check != null) {
					for (int i = 0;i<check.size();i++) {
						int a = check.get(i);
						if (!visited[a]) {
							visited[a] = true;
							deque.add(a);
						}
					}
				}
			}
			
		}
		
		System.out.println(cnt);
		
		
	}
}
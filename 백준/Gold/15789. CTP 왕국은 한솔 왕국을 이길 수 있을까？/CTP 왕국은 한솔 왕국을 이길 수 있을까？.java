import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Stack;
import java.util.StringTokenizer;


public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		Map<Integer, ArrayList<Integer>> nodes = new HashMap<>();
		
		// nodes 받기
		for (int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			if (!nodes.containsKey(x)) {
				nodes.put(x, new ArrayList<Integer>());
			}
			nodes.get(x).add(y);
			if (!nodes.containsKey(y)) {
				nodes.put(y, new ArrayList<Integer>());
			}
			nodes.get(y).add(x);
		}
		
		
		List<Integer> powers = new ArrayList<>();
		boolean[] visited = new boolean[N+1];
		
		st = new StringTokenizer(br.readLine());
		int ctpNum = Integer.parseInt(st.nextToken());
		int hanNum = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		int ctp = 0;
		int han = 0;
		
		for (int i=1;i<N;i++) {
			if (!visited[i]) {
				visited[i] = true;
				Stack<Integer> stack = new Stack<>();
				Set<Integer> set = new HashSet<>();
				stack.add(i);
				set.add(i);
				while (!stack.isEmpty()) {
					int s = stack.pop();
					ArrayList<Integer> li = nodes.get(s);
					
					if (li != null) {
						for (int j:li) {
							if (!visited[j]) {
								stack.add(j);
								set.add(j);
								visited[j] = true;
							} 
						}
					}
				}
				
				if (set.contains(ctpNum)) {
					ctp = set.size();
				} else if (set.contains(hanNum)) {
					han = set.size();
				} else {
					powers.add(set.size());
				}
			} else continue;
		}
		
		Collections.sort(powers, Collections.reverseOrder());
		
		
		// System.out.println(powers);
		
		
		for (int i=0;i<k;i++) {
			ctp += powers.get(i);
		}
		

		System.out.println(ctp);
		


		// System.out.println(len);

		
	}
}
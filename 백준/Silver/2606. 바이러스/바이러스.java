import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		Map<Integer, int[]> map = new HashMap<>();
		
		for (int i=1;i<=N;i++) {
			int[] tmp = new int[N];
			map.put(i, tmp);
		}
		
		for (int i=0;i<M;i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int k = Integer.parseInt(st.nextToken());
			int s =  Integer.parseInt(st.nextToken());
			int[] tmp1 = map.get(k);
			int[] tmp2 = map.get(s);
			
			tmp1[s-1] = 1;
			tmp2[k-1] = 1;
			
			map.replace(k, tmp1);
			map.replace(s, tmp2);

		}
		
		Deque<Integer> check = new ArrayDeque<>();
		Set<Integer> virus = new HashSet<>();
		
		int[] n1 = map.get(1);
		virus.add(1);
		for (int i=0;i<N;i++) {
			if (n1[i] == 1) check.add(i+1);
		}
		
		// check 가 없어지기 전까지
		while (!(check.isEmpty())) {
			int b = check.removeFirst();
			virus.add(b);
			
			int[] connect = map.get(b);
			for (int i=0;i<N;i++) {
				if (connect[i] == 1 && !(virus.contains(i+1))) {
					check.add(i+1);
				}
			}
		}
		
		System.out.println(virus.size()-1);

		
		
	}

}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] fruit = new int[N];
		
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i=0;i<N;i++) {
			int s = Integer.parseInt(st.nextToken());
			fruit[i] = s;
		}
		
		int start = 0;
		int end = 0;
		int max = 0;
		
		Map<Integer, Integer> fruitCount = new HashMap<>();
		
				
		while (end < N) {
			fruitCount.put(fruit[end], fruitCount.getOrDefault(fruit[end], 0)+1);
			
			while (fruitCount.size() > 2) {
				fruitCount.put(fruit[start], fruitCount.get(fruit[start])-1);
				if (fruitCount.get(fruit[start]) == 0) {
					fruitCount.remove(fruit[start]);
				}
				start++;
			}
			
			max = Math.max(max, end-start+1);
			
			end++;
				
			
			
		}

		System.out.println(max);

		
	}
}
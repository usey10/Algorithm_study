import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		
		for (int tc=1;tc<=T;tc++) {
			int k = Integer.parseInt(br.readLine());
			Set<String> wear = new HashSet<>();
			Map<String, Integer> map = new HashMap<>();
			
			for (int i=1;i<=k;i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				String name = st.nextToken();
				String ctg = st.nextToken();
				wear.add(ctg);
				if (map.containsKey(ctg)) {
					map.replace(ctg, map.get(ctg)+1);
				} else {
					map.put(ctg, 1);
				}
				
			}
			
			int sum = 1;
			for (String s :wear) {
				sum *= map.get(s) + 1;
			}
			sb.append(sum-1).append("\n");
			
			
		}

		
		System.out.println(sb);

	}
}

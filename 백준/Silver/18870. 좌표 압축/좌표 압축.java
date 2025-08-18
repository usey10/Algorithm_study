import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		Set<Long> set = new TreeSet<>();
		long[] arr = new long[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i=0;i<N;i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			
			set.add(arr[i]);
		}
		

		Map<Long,Integer> map = new HashMap<>();

		Iterator<Long> iterator = set.iterator();

		for (int i=0;i<set.size();i++) {
			long c = iterator.next();
			map.put(c, i);
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (long k:arr) {
			sb.append(map.get(k)).append(" ");
		}
		
		System.out.println(sb.toString());

		
	}
}
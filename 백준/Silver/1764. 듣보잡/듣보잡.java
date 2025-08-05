import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		Set<String> her = new HashSet<>();
		Set<String> see = new HashSet<>();
		for (int i=0;i<n;i++) {
			her.add( br.readLine());
		}
		for (int i=0;i<m;i++) {
			see.add( br.readLine());
		}
		
		her.retainAll(see);
		
		sb.append(her.size()).append("\n");
		
		String[] arr = new String[her.size()];
		her.toArray(arr);
		Arrays.sort(arr);
		for (String a:arr) {
			sb.append(a).append("\n");
		}
		
		System.out.print(sb);


		
	}
}

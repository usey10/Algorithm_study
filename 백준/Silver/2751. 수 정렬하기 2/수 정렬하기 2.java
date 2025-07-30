import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		
		List<Integer> nSet = new ArrayList<>();
		
		for (int i=0;i<N;i++) {
			nSet.add(Integer.parseInt(br.readLine()));
		}
		
		Collections.sort(nSet);
		
		for (int li : nSet) {
			sb.append(li);
			sb.append("\n");
		}
		
		System.out.println(sb);

	}
}
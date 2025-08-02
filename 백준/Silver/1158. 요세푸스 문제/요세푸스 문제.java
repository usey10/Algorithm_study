import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


public class Main {
	public static void main(String[] arge) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		String[] lines = br.readLine().split(" ");
		int n = Integer.parseInt(lines[0]);
		int k = Integer.parseInt(lines[1]);

		List<Integer> nSet = new ArrayList<>();
		for (int i=0;i<n;i++){
			nSet.add(i+1);
		}

		int idx = 0;
		sb.append("<");
		for (int i =0;i<n;i++){
			idx += k-1;
			idx %= nSet.size();
			sb.append(nSet.get(idx));
			if (i < n-1) sb.append(", ");
			nSet.remove(idx);
		}
		sb.append(">");

		System.out.println(sb);
		

	}
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String num = "666";
		
		List<Integer> sixSet = new ArrayList<>();
		
		int N = Integer.parseInt(br.readLine());
		
		for (int i=1;i<10000000;i++) {
			if (String.valueOf(i).contains("666")) {
				sixSet.add(i);
				
				if (sixSet.size() == N) {break;}
			}
		}
		

		System.out.println(sixSet.get(N-1));


	}
}
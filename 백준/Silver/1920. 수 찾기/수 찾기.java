import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		String[] nums = br.readLine().split(" ");
		Set<Integer> nSet = new HashSet<>();
		
		for (int i=0;i<N;i++) {
			nSet.add(Integer.parseInt(nums[i]));
		}
		
		int M = Integer.parseInt(br.readLine());
		
		String[] check = br.readLine().split(" ");
		
		for (int i=0; i<M;i++) {
			int result = 0;
			if (nSet.contains(Integer.parseInt(check[i]))) {
				result = 1;
			}
			System.out.println(result);
		}


	}
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		int K = Integer.parseInt(br.readLine());
		
		int sum = 0;
		Deque<Integer> stack = new ArrayDeque<>();
		
		for (int i=0;i<K;i++) {
			int num = Integer.parseInt(br.readLine());
			if (num == 0) {
				sum -= stack.removeLast();
			} else {
				sum += num;
				stack.add(num);
			}
		}
		
		System.out.println(sum);
		

	}
}

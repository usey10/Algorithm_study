import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		
		PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
		
		for (int i=0;i<N;i++) {
			int cal = Integer.parseInt(br.readLine());

			if (cal == 0) {
				if (queue.size() == 0) sb.append(0).append("\n");
				else {
				int k = queue.remove();
				sb.append(k).append("\n");
				}
			}
			else {
				queue.add(cal);
			}
		}
		
		System.out.println(sb);


		
	}
}

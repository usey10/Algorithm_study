import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> queue = new PriorityQueue<>();
		PriorityQueue<Integer> minerQueue = new PriorityQueue<>();
		
		for (int tc=1;tc<=T;tc++) {
			int k = Integer.parseInt(br.readLine());
			if (k > 0) {
				queue.add(k);
			} else if (k < 0) {
				minerQueue.add(-k);
			} else {
				int k1=0;
				int k2=0;
				
				if (!(queue.isEmpty())) {
					k1 = queue.poll();
				} 
				if (!(minerQueue.isEmpty())) {
					k2 = minerQueue.poll();
				}
				
				if (k1*k2!=0) {
					if (k1 >= k2) {
						sb.append(-k2).append("\n");
						queue.add(k1);
					}
					else {
						sb.append(k1).append("\n");
						minerQueue.add(k2);
					}
				}
				else if (k1 + k2 == 0) {
					sb.append(0).append("\n");
				}
				else if (k1 == 0) {
					sb.append(-k2).append("\n");					
				} else  {
					sb.append(k1).append("\n");
				}
			}
			
		}

		
		System.out.println(sb);

	}
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		
		Deque<Integer> queue = new ArrayDeque<>();
		
		for (int i=0;i<N;i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			String odr = st.nextToken();
			
			if (odr.equals("push_back")) {
				queue.addLast(Integer.parseInt(st.nextToken()));
			} else if (odr.equals("push_front")) {
				queue.addFirst(Integer.parseInt(st.nextToken()));
			} else if (odr.equals("pop_front")) {
				sb.append(queue.isEmpty()? -1:queue.removeFirst()).append("\n");
			} else if (odr.equals("pop_back")) {
				sb.append(queue.isEmpty()? -1:queue.removeLast()).append("\n");
			} else if (odr.equals("size")) {
				sb.append(queue.size()).append("\n");
			} else if (odr.equals("empty")) {
				sb.append(queue.isEmpty()? 1:0).append("\n");
			} else if (odr.equals("front")) {
				sb.append(queue.isEmpty()? -1:queue.peekFirst()).append("\n");
			} else if (odr.equals("back")) {
				sb.append(queue.isEmpty()? -1:queue.peekLast()).append("\n");
			}

		}
		
		System.out.println(sb);


		
	}
}

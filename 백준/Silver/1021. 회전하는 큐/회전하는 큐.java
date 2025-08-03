import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	public static int queuepop(int i, Deque<Integer> queue) {
		int cnt = 0;
		while (true) {
			int k = queue.removeFirst();
			if(k == i) {
				break;
			} else {
				queue.add(k);
				cnt++;
			}
		}
		if (cnt <= queue.size()/2) return cnt;
		else return (queue.size() - cnt +1);
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		Deque<Integer> deque = new ArrayDeque<>();
		
		for (int i=0;i<N;i++) {
			deque.add(i+1);
		}
		
		int move = 0;
		
		String[] lines = br.readLine().split(" ");
		for (String li:lines) {
			
			move += queuepop(Integer.parseInt(li), deque);
		}
		
		System.out.println(move);

	}
}

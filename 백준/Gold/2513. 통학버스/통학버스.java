import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class mComparator implements Comparator<int[]> {
	@Override
	public int compare(int[] a, int[] b) {
		return a[0] - b[0];
	}
}
class pComparator implements Comparator<int[]> {
	@Override
	public int compare(int[] a, int[] b) {
		return b[0] - a[0];
	}
}
public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		
		PriorityQueue<int[]> pqPlus = new PriorityQueue<>(new pComparator());
		PriorityQueue<int[]> pqMinus = new PriorityQueue<>(new mComparator());
				
		
		for (int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			int[] tmp = new int[2];
			tmp[0] = Integer.parseInt(st.nextToken()) - S;
			tmp[1] = Integer.parseInt(st.nextToken());
			if (tmp[0] > 0) pqPlus.add(tmp);
			else pqMinus.add(tmp);
		}
		
		
		long len = 0;
		
		int child = 0;
		int max = 0;
		
		// 학교 기준 양수
		while (!pqPlus.isEmpty()) {
			// child 가 다 차면 다음을 넘어갈 수 있도록 초기
			if (child == K) {
				len += max * 2;
				max = 0;
				child = 0;
			}
			
			// child 넣기
			int[] go = pqPlus.poll();
			
			if (child + go[1] <= K) { // go[1] 을 다 넣을 수 있는 경우
				max = Math.max(max, go[0]);
				child += go[1];
			} else { // go[1] 을 다 넣을 수 없는 경우
				max = Math.max(max, go[0]);
				go[1] -= K - child;
				child = K;
				pqPlus.add(go); // 다시 뺄 수 있게 넣기
			}

		}
		
		
		if (child != 0) {
			len += max * 2;
			child = 0;
			max = 0;
		}
		
		
		// 학교 기준 음수
		while (!pqMinus.isEmpty()) {
			// child 가 다 차면 다음을 넘어갈 수 있도록 초기
			if (child == K) {
				len += max * 2;
				max = 0;
				child = 0;
			}
			
			// child 넣기
			int[] go = pqMinus.poll();
			
			if (child + go[1] <= K) { // go[1] 을 다 넣을 수 있는 경우
				max = Math.max(max, -go[0]);
				child += go[1];
			} else { // go[1] 을 다 넣을 수 없는 경우
				max = Math.max(max, -go[0]);
				go[1] -= K - child;
				child = K;
				pqMinus.add(go); // 다시 뺄 수 있게 넣기
			}
			
		}
		
		
		if (child != 0) {
			len += max * 2;
			child = 0;
			max = 0;
		}
		


		System.out.println(len);

		
	}
}
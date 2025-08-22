import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String lines = br.readLine();
		
		Deque<Integer> deque = new ArrayDeque<>();
		boolean plus = false;
		int num = 0;
		
		for (int i=0;i<lines.length();i++) {
			char k = lines.charAt(i);
			if (k >= 48) num = num*10 + (k-'0');
			else if (k == '+' && plus) {
				int a = deque.pollLast();
				deque.add(num + a);
				num=0;
			} else if (k == '+') {
				plus = true;
				deque.add(num);
				num=0;
			} else if (k=='-' && plus){
				int a = deque.pollLast();
				deque.add(num + a);
				plus = false;
				num=0;
			} else {
				deque.add(num);
				num=0;
			}
				
		}
		
		
		// 마지막 값 연산
		if (plus) {
			int a = deque.pollLast();
			num = num+a;
		}
		
		deque.add(num);
		
		
		
		num = deque.pollFirst();
		
		while (!deque.isEmpty()) {
			int a = deque.pollFirst();
			num -= a;
		}
		
		
		System.out.println(num);
	}

}

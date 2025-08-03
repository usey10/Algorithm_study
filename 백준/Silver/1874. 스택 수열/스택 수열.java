import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());

		Deque<Integer> stack = new ArrayDeque<>();
		String res = "";
		int startNum = 1;
		
		for (int i=0;i<N;i++) {
			int target = Integer.parseInt(br.readLine());
			
			while (true) {
//				System.out.println(stack.toString());
				if (startNum < target) {
					stack.add(startNum++);
					sb.append("+").append("\n");	
				} else if (startNum > target) {
					if (stack.removeLast() == target) {
						// pop의 경우 무조건 타겟이랑 같아야 함.
						sb.append("-").append("\n");
						break;
					} else {
						// 타겟이랑 다름 -> 불가
						res = "NO";
						break;
					}
				}else { // target == startNum
					stack.add(startNum++);
					stack.removeLast();
					sb.append("+").append("\n");	
					sb.append("-").append("\n");
					break;
				}
				
			}
			
			if (res.equals("NO")) break;
		}
		
		System.out.print((res.equals("NO"))? res:sb.toString());
		
	}
}

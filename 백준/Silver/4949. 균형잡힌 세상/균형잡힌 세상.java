import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		while (true){
			String lines = br.readLine();

			if (lines.equals(".")) break;
			String res = "yes";
			Stack<Character> stack = new Stack<>();

			for (int i=0;i<lines.length();i++) {
				char k = lines.charAt(i);
				if (k == '(' || k == '[' ){
					stack.add(k);
				}
				else if (k == ')'){
					if (stack.isEmpty()) {
						res = "no"; 
						break;
					} else if (stack.pop() != '(') {
						res = "no";
						break;
					} else {
						continue;
					}
				}
				else if (k == ']'){
					if (stack.isEmpty()) {
						res = "no"; 
						break;
					} else if (stack.pop() != '[') {
						res = "no";
						break;
					} else {
						continue;
					}
					
				}
				else continue;
			}

			if (stack.isEmpty()){
				sb.append(res);
			} else sb.append("no");
			sb.append("\n");
		}

		sb.delete(sb.length()-1, sb.length());
		System.out.println(sb);
		
	}
}

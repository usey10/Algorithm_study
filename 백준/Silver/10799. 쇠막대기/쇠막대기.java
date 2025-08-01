import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


public class Main {
	public static void main(String[] arge) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] lines = br.readLine().split("");
		
		List<String> stack = new ArrayList<>();
		
		String before = "x";
		int count = 0;
		for (int i=0;i<lines.length;i++) {
			
			if (lines[i].equals("(")){
				stack.add(lines[i]);
			}
			else if (lines[i].equals(")")) {
				if (before.equals("(")) {
					stack.remove(stack.size()-1);
					count += stack.size();
				} else {
					stack.remove(stack.size()-1);
					count += 1;
				}
			}
//			System.out.println("before : " + before + ", count : " + count + ", stack : " + stack.toString());
			before = lines[i];
		}
		
		System.out.println(count);
	}
}

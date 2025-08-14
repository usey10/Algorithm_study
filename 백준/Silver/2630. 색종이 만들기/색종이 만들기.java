import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Stack;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		
		String[][] paper = new String[N][];
		for (int i=0;i<N;i++) {
			paper[i] = br.readLine().split(" ");
		}
		
		
		Stack<String[][]> stack = new Stack<>();
		
		stack.add(paper);
		int cntWhite = 0;
		int cntBlue = 0;
		while (!stack.isEmpty()) {
			
			String[][] checkPaper = stack.pop();
			String check = checkPaper[0][0];
			boolean one = true;
			
			for (int i=0;i<checkPaper.length;i++) {
				for (int j=0;j<checkPaper.length;j++) {
					if (!checkPaper[i][j].equals(check)) {
						one = false;
						break;
					}
				}
				if (!one) break;
			}
			
			if (!one) {
				int range = checkPaper.length/2;
				String[][] p1 = new String[range][range];
				String[][] p2 = new String[range][range];
				String[][] p3 = new String[range][range];
				String[][] p4 = new String[range][range];
				
				for (int r=0;r<checkPaper.length/2;r++) {
					for (int c=0;c<checkPaper.length/2;c++) {
						p1[r][c] = checkPaper[r][c];
						p2[r][c] = checkPaper[r+range][c];
						p3[r][c] = checkPaper[r][c+range];
						p4[r][c] = checkPaper[r+range][c+range];
					}
				}
				stack.add(p1);
				stack.add(p2);
				stack.add(p3);
				stack.add(p4);
			}
			else {
				if (checkPaper[0][0].equals("1")) cntBlue++;
				else cntWhite++;
			}
		}
		
		sb.append(cntWhite).append("\n").append(cntBlue);
		
		System.out.println(sb.toString());
		
		
		
	}
}
import java.util.Arrays;
import java.util.Scanner;
import java.io.FileInputStream;
import java.util.Stack;

class Solution
{
	static String[][] trees;
	static Stack<Integer> stack;
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = 10;

		for(int tc = 1; tc <= T; tc++)
		{
			// 2차원 배열로 받기
			int N = sc.nextInt();
			sc.nextLine();
			// tree 받기
			trees = new String[N+1][];
			stack = new Stack<>();
			
			for (int i=1;i<=N;i++) {
				String[] lines = sc.nextLine().split(" ");
				String[] tmp = new String[3];
				
				tmp[0] = lines[1];
				
				if (lines.length == 3) {
					tmp[1] = lines[2];
					tmp[2] = " ";
				}
				else if (lines.length == 4) {
					tmp[1] = lines[2];
					tmp[2] = lines[3];
				} else {
					tmp[1] = " ";
					tmp[2] = " ";
				}
				
				trees[i] = tmp;
			}
			
//			System.out.println('-' + 0);
//			System.out.println('+' + 0);
//			System.out.println('/' + 0);
//			System.out.println('*' + 0);
//			System.out.println('0' + 0);
			
			// System.out.println(Arrays.deepToString(trees));
			// System.out.println(stack);
			postOrder("1");
			
			System.out.println("#" + tc + " " + stack.pop());
			

		}
	}
	
	static void postOrder(String x) {
		// System.out.println(x);
		
		if ( !x.equals(" ") && Integer.parseInt(x) < trees.length) {
			int k = Integer.parseInt(x);
			postOrder(trees[k][1]);
			postOrder(trees[k][2]);
			
			// 숫자, 연산자 구분
			if (trees[k][0].equals("+")) {
				int x1 = stack.pop();
				int x2 = stack.pop();
				stack.push(x1+x2);
			} else if (trees[k][0].equals("-")) {
				int x1 = stack.pop();
				int x2 = stack.pop();
				stack.push(x2-x1);
			} else if (trees[k][0].equals("*")) {
				int x1 = stack.pop();
				int x2 = stack.pop();
				stack.push(x1*x2);
			} else if (trees[k][0].equals("/")) {
				int x1 = stack.pop();
				int x2 = stack.pop();
				stack.push(x2/x1);
			} else {
				stack.push(Integer.parseInt(trees[k][0]));
			}
//			System.out.println(stack);

		}
	}
}
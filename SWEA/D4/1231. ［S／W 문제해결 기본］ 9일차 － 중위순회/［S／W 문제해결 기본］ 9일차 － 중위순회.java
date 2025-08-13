import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	static String[] trees;
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=10;

		for(int tc = 1; tc <= T; tc++)
		{
			StringBuilder sb = new StringBuilder();
			int N = sc.nextInt();
			sc.nextLine();
			// tree 받기
			trees = new String[N+1];
			for (int i=1;i<=N;i++) {
				String[] lines = sc.nextLine().split(" ");
				trees[i] = lines[1];
			}
			
			inOrder(1, sb);
			
			System.out.println("#" + tc + " " + sb.toString());
			

		}
	}
	
	static void inOrder(int x, StringBuilder sb) {
		if (x < trees.length && !trees[x].equals(null)) {
			inOrder(x*2, sb);
			sb.append(trees[x]);
			inOrder(x*2+1, sb);
		}
	}
}
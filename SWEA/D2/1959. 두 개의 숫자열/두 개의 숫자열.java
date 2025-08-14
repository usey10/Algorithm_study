import java.util.Arrays;
import java.util.Scanner;
import java.io.FileInputStream;
import java.util.Deque;
import java.util.List;
import java.util.ArrayDeque;
import java.util.ArrayList;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		StringBuilder sb = new StringBuilder();

		for(int tc = 1; tc <= T; tc++)
		{
			int A = sc.nextInt();
			int B = sc.nextInt();
			
			int num = Math.abs(A - B) + 1;
			
			int[] aSet = new int[A];
			int[] bSet = new int[B];
			
			for (int i=0;i<A;i++) {
				aSet[i] = sc.nextInt();
			}
			for (int i=0;i<B;i++) {
				bSet[i] = sc.nextInt();
			}
			
			int max = 0;
			for (int i=0;i<num;i++) {
				if (A < B) {
					int sum = 0;
					for (int j=0;j<A;j++) {
						sum += aSet[j] * bSet[j+i];
					}
					max = Math.max(max, sum);
				} else {
					int sum = 0;
					for (int j=0;j<B;j++) {
						sum += aSet[j+i] * bSet[j];
					}
					max = Math.max(max, sum);
				}
			}
			
			sb.append("#").append(tc).append(" ").append(max).append("\n");
		}
		
		System.out.print(sb.toString());
	}
	
	
	
}
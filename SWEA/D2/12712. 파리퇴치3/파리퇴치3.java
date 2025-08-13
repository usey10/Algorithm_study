import java.io.FileInputStream;
import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for (int tc = 1; tc <= T; tc++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			
			int[][] arr = new int[N][N];
			
			for (int i=0;i<N;i++) {
				for (int j=0;j<N;j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			//System.out.println(Arrays.deepToString(arr));
			//System.out.println(N + "," + M);
			
			int max = 0;
			
			for (int i=0;i<N;i++) {
				for (int j=0;j<N;j++) {
					int cnt = arr[i][j];
					// 직각 
					for (int x = 1; x <= M-1;x++) {
						if (i-x >= 0) cnt += arr[i-x][j];
						if (i+x < N) cnt += arr[i+x][j];
						if (j-x >= 0) cnt += arr[i][j-x];
						if (j+x < N) cnt += arr[i][j+x];
					}
					
					max = Math.max(max, cnt);
					
					cnt = arr[i][j];
					// 대각선 
					for (int x = 1; x <= M-1;x++) {
						if (i-x >= 0 && j-x >= 0) cnt += arr[i-x][j-x];
						if (i-x >= 0 && j+x < N) cnt += arr[i-x][j+x];
						if (i+x < N && j-x >= 0) cnt += arr[i+x][j-x];
						if (i+x < N && j+x < N) cnt += arr[i+x][j+x];
					}
					
					max = Math.max(max, cnt);
					
				}
			}
			
			

			System.out.println("#" + tc + " " + max);
		}
	}
}
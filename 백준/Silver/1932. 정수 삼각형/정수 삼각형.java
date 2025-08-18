import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		
		int[][] board = new int[N][];
		long[][] sumBoard = new long[N][];
		
		for (int i=0;i<N;i++) {
			String[] line = br.readLine().split(" ");
			
			int[] newBoard = new int[line.length];
			long[] newSum = new long[line.length];
			
			for (int j = 0;j<line.length;j++) {
				newBoard[j] = Integer.parseInt(line[j]);
//				System.out.println(j + ", " + newBoard[j]);
				
				if (i == 0) newSum[j] = newBoard[j];
				else {
					if (j == 0) {
						newSum[j] = sumBoard[i-1][j] + newBoard[j];
					} else if (j == line.length-1) {
							newSum[j] = sumBoard[i-1][j-1] + newBoard[j];
					} else {
						newSum[j] = Math.max(sumBoard[i-1][j-1], sumBoard[i-1][j]) + newBoard[j];
					}
				}
			}
			
			board[i] = newBoard;
			sumBoard[i] = newSum;
		}
		
		long max = Long.MIN_VALUE;
		for (int i=0;i<sumBoard[N-1].length;i++) {
			if (sumBoard[N-1][i] > max) max = sumBoard[N-1][i];
		}
		System.out.println(max);
		
	}
}
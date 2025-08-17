import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		long B = Integer.parseInt(st.nextToken());
		
		int[][] board = new int[N][M];
		long sum = 0;
		for (int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			
			for (int j=0;j<M;j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
				sum += board[i][j];
			}
		}
		
		sum += B;
		sum =  sum / (N*M);
		int maxH = (sum > 256)? 256:(int)sum;
		
		long[] min = {257, Long.MAX_VALUE};
		for (int h=maxH;h>=0;h--) {
			long time = 0;
			
			for (int i = 0; i< N;i++) {
				for (int j=0;j<M;j++) {
					if (board[i][j] > h) {
						time += (board[i][j] - h)*2;
					} else {
						time += h - board[i][j];
					}
					
				}
				if (time > min[1]) break;
			}
			
			if (time < min[1]) {
				min[0] = h;
				min[1] = time;
			}
			
		}
		
		
		System.out.println(min[1] + " " + min[0]);
		
	}
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		long[][] small = new long[N+1][3];
		
		for (int i=0;i<N;i++) {
			String[] lines = br.readLine().split(" ");
			int R = Integer.parseInt(lines[0]);
			int G = Integer.parseInt(lines[1]);
			int B = Integer.parseInt(lines[2]);
			
			small[i+1][0] = Math.min(small[i][1], small[i][2]) + R;
			small[i+1][1] = Math.min(small[i][0], small[i][2]) + G;
			small[i+1][2] = Math.min(small[i][0], small[i][1]) + B;
			
		}
		
		
		long check = Math.min(Math.min(small[N][0], small[N][1]), small[N][2]);
		
		System.out.println(check);
		
	}
}
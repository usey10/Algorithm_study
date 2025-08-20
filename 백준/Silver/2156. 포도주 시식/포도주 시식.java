import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		
		int[] nset = new int[N];
		
		
		for (int i=0;i<N;i++) {
			nset[i] = Integer.parseInt(br.readLine());
		}
		
		
		
		int[][] wines = new int[N][3];
		
		wines[0][1] = nset[0];
		
		for (int i = 1;i<N;i++) {
			wines[i][0] = Arrays.stream(wines[i-1]).max().getAsInt();
			wines[i][1] = wines[i-1][0] + nset[i];
			wines[i][2] = wines[i-1][1] + nset[i];
			
		}
		
		System.out.println(Arrays.stream(wines[N-1]).max().getAsInt());
	}

}

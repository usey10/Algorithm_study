import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		long[][] nset = new long[N][2];
		
		nset[0][0] = 0; // 끝이 0인 개수
		nset[0][1] = 1; // 끝이 1인 개수
		
		
		
		for (int i=1;i<N;i++) {
			nset[i][0] = nset[i-1][1] + nset[i-1][0];
			nset[i][1] = nset[i-1][0];
		}
		
		
		
		System.out.println(nset[N-1][0] + nset[N-1][1]);
	}

}

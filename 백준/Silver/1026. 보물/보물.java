import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		int[] A = new int[N];
		int[] B = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for (int j=0;j<N;j++) {
			A[j] = Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		for (int j=0;j<N;j++) {
			B[j] = Integer.parseInt(st.nextToken());
		}
		
		int[] c = Arrays.copyOf(B, N);
		Arrays.sort(c);
		
		Arrays.sort(A);
		
		int sum = 0;
		
		for (int i=0;i<N;i++) {
			sum += c[i]*A[N-i-1];
		}


		System.out.println(sum);
		

		
	}
}
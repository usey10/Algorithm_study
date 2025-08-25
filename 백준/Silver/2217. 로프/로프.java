import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] ropes = new int[N];
		for (int i=0;i<N;i++) {
			ropes[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(ropes);
		
		long max = Integer.MIN_VALUE;
		for (int i=0;i<N;i++) {
			max = Math.max(max, ropes[N-1-i] * (i+1));
		}
		
		System.out.println(max);
	}

}

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		String[] scores = br.readLine().split(" ");
		int[] intSc = new int[N];
		
		int maxSc = 0;
		for (int i=0;i<N;i++) {
			intSc[i] = Integer.parseInt(scores[i]);
			if(maxSc<intSc[i]) {
				maxSc = intSc[i];
			}
		}
		
		double newScSum = 0;
		
		for (int el:intSc) {
			newScSum += ((double) el/maxSc)*10000;
		}
		
		System.out.println((double)(newScSum/100)/N);
		
	}
}
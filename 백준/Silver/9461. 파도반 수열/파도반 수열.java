import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		long[] p = new long[101];
		p[0] = 0;
		long[] firstP = {0,1,1,1,2,2,3,4,5,7,9};
		
		for (int i=1;i<=100;i++) {
			if (i <= 10) {
				p[i] = firstP[i];
			} else {
				p[i] = p[i-1] + p[i-5];
			}
		}
		
		for (int tc=0;tc<T;tc++) {
			int N = Integer.parseInt(br.readLine());
			sb.append(p[N]).append("\n");
		}
		
		System.out.println(sb);

		
	}

}
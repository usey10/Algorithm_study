import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class SumAB{
	
	public static int sumResult(String line){
		StringTokenizer st = new StringTokenizer(line);
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		return A + B;
	}
	
}

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int i=0;i<T;i++) {
			String cs = br.readLine();
			
			int result = SumAB.sumResult(cs);
			sb.append(result);
			sb.append("\n");
		}
		System.out.print(sb);
	}
}
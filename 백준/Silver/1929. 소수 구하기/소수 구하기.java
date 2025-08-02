import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static boolean dem(int x) {
		if (x==1) return false;
		for (int i = 1; i <= Math.sqrt(x); i++) {
			if (i != 1 && x%i == 0) return false;
		}
		return true;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());


		for (int i = M; i <= N; i++) {
			if (dem(i)) sb.append(i).append("\n");
		}

		System.out.print(sb.toString());
		br.close();

	}
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int n = Integer.parseInt(br.readLine());
		
		int[][] dots = new int[n][2];
		
		for (int i=0;i<n;i++) {
			String[] lines = br.readLine().split(" ");
			dots[i][0] = Integer.parseInt(lines[0]);
			dots[i][1] = Integer.parseInt(lines[1]);
		}
		
		Arrays.sort(dots, (x1, x2) -> {
			if (x1[0] == x2[0]) {
				return x1[1] - x2[1];
				} 
			return (x1[0] - x2[0]);
			});
		
		for (int[] d:dots) {
			sb.append(d[0] + " " + d[1] + "\n");
		}
		
		System.out.println(sb.toString());

	}
}
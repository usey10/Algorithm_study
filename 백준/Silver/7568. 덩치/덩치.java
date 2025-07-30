import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		
		int[][] nSet = new int[N][2];

		
		for (int i=0;i<N;i++) {
			String[] lines = br.readLine().split(" ");
			nSet[i][0] = Integer.parseInt(lines[0]);
			nSet[i][1] = Integer.parseInt(lines[1]);
		}
		
		int[] ranks = new int[N];
		
		for (int i=0;i<N;i++) {
			int rank = 1;
			for (int j=0;j<N;j++) {
				if (j==i) continue;
				else {
					if (nSet[i][0] < nSet[j][0] && nSet[i][1] < nSet[j][1]) rank++;
					
				}
			}
			ranks[i] = rank;
		}

		for (int li : ranks) {
			sb.append(li);
			sb.append(" ");
		}
		
		System.out.println(sb);

	}
}
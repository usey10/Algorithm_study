import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[][] nset = new int[N][N];
		int[] nowNum = new int[N];
		
		for (int i=0;i<N;i++) {
			nowNum[i] = N-1; // 마지막 부터 확인 번호 저장
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j=0;j<N;j++) {
				nset[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int cnt = 0;
		int result = 0;
		while (cnt < N) {
			int[] maxSet = new int[2];
			maxSet[1] = Integer.MIN_VALUE;
			for (int i=0;i<N;i++) {
				if (maxSet[1] < nset[nowNum[i]][i]) {
					maxSet[0] = i;
					maxSet[1] = nset[nowNum[i]][i];
				}
			}
			// System.out.println(Arrays.toString(maxSet));
			// System.out.println(Arrays.toString(nowNum));
			
			cnt++;
			result = maxSet[1];
			nowNum[maxSet[0]] -= 1;
		}
		
		System.out.println(result);
		
		

		
	}

}
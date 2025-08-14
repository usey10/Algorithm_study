import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] trees = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i=0;i<N;i++) {
			trees[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(trees);
		
		int cutResult = 0;
		int line = trees[N-1];
		int idx = 1;
		while (cutResult < M) {
			if (idx < N) {
				int check = line - trees[N-idx-1];
				int get = (M-cutResult)/idx;
				
				if (check > get && get*idx >= M - cutResult) {
					cutResult += get*idx;
					line -= get;
				} else if (check > get && get*idx < M - cutResult) {
					cutResult += get*idx + idx;
					line -= get + 1;
				} else {
					cutResult += idx * check;
					line -= check;
				}
				idx++;
				
			} else {
				int get = (M-cutResult)/N;
				
				if (get*N >= M - cutResult) {
					cutResult += get*N;
					line -= get;
				} else {
					cutResult += get*N + N;
					line -= get +1;
				}
			}
			
		}
		
		System.out.println(line);
		
		
	}
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		int[] nLine = new int[n];
		long allSum = 0;
		long min = Integer.MAX_VALUE;
		for (int i=0;i<n;i++) {
			nLine[i] = Integer.parseInt(br.readLine());
			allSum += nLine[i];
			if (min > nLine[i]) min = nLine[i];
		}
		
		int t = k/n ;
		if (k % n != 0) t += 1;
		
		long sMin = 1; 
		long sMax = allSum  / k;  //
//		System.out.println(sMin + ", " + sMax );
		long result = 0;
		while (sMin <= sMax) {
			int cnt = 0;
//			if (sMax < sMin) break;
			long s = (sMax+sMin) / 2;
			if (s==0) s = 1;
			
			for (int i=0;i<n;i++) {
				cnt += nLine[i] / s;
//				System.out.print(nLine[i] % s+ " ");
			}
//			System.out.println();
			if (cnt >= k) {
				
//				if (sMin >= sMax || sMin == s) {
//					result = s;
//					break;
//				}

				result = s;
				sMin = s+1;
			}
			else {
				// 더 획기적으로 줄여야 함..
				//s--;
//				if (sMin >= sMax) {
//					result = s;
//					break;
//				}
				sMax = s-1;
			}
		}
		
	
		System.out.println(result);

	}
}

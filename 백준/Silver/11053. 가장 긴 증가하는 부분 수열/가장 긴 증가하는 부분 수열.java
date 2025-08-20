import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int[] m;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] list = new int[N];
		for (int i=0;i<N;i++) {
			list[i] = Integer.parseInt(st.nextToken());
		}
		
		m = new int[N];
		
		m[0] = 1;
		for (int i=1;i<N;i++) {
			for (int j=0;j<i;j++) {
				if (list[j] < list[i]) {
					m[i] = Math.max(m[j], m[i]);
				}
			}
			m[i] += 1;
		}
		
		System.out.println(Arrays.stream(m).max().getAsInt());
	}

}

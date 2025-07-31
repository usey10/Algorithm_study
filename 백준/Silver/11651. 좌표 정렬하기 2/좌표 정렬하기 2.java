import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		
		List<int[]> dots = new ArrayList<>();
		
		for (int i=0;i<n;i++) {
			String[] lines = br.readLine().split(" ");
			int x = Integer.parseInt(lines[0]);
			int y = Integer.parseInt(lines[1]);
			int[] xy = {x,y};
			dots.add(xy);
		}
		
		Collections.sort(dots, new Comparator<int[]>() {
			@Override
			public int compare(int[] a, int[] b) {
				if (a[1] == b[1]) {
					return a[0] - b[0];
				}
				return a[1] - b[1];
			}
		});
		

		for (int[] d:dots) {
			bw.append(d[0] + " " + d[1]);
			bw.newLine();
		}
		
		bw.flush();
		bw.close();
		br.close();

	}
}
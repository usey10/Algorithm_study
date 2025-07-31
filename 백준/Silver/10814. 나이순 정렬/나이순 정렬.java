import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int n = Integer.parseInt(br.readLine());
		
		List<String[]> members = new ArrayList<>();
		
		for (int i=0;i<n;i++) {
			members.add(br.readLine().split(" "));
		}
		
		Collections.sort(members, new Comparator<String[]>() {
			public int compare(String[] x1, String[] x2) {
				if (Integer.parseInt(x1[0]) == Integer.parseInt(x2[0])) {
					return 0;
				} 
				return (Integer.parseInt(x1[0]) - Integer.parseInt(x2[0]));
			}
		});
		
		for (String[] m:members) {
			System.out.println(m[0] + " " + m[1]);
		}
	}
}
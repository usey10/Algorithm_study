import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		
		Set<Integer> set = new HashSet<>();
		int M = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < M; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String order = st.nextToken();
			
			if (order.equals("add")) {
				set.add(Integer.parseInt(st.nextToken()));
			} else if (order.equals("remove")) {
				// 파이썬과 다르게 이렇게 쓰면 무시된다!
				set.remove(Integer.parseInt(st.nextToken()));
			} else if (order.equals("toggle")) {
				int check = Integer.parseInt(st.nextToken());
				if (set.contains(check)) set.remove(check);
				else set.add(check); // 없는 경우
			} else if (order.equals("all")) {
				set.clear();
				for (int k=1;k<=20;k++) set.add(k);
			} else if (order.equals("empty")) {
				set.clear();
			} else if (order.equals("check")) {
				sb.append((set.contains(Integer.parseInt(st.nextToken())))?1:0);
				sb.append("\n");
			}
			

			
		}
		System.out.print(sb);
		

	}
}

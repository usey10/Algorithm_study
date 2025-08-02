import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringBuilder sb = new StringBuilder();


		int N = Integer.parseInt(br.readLine());
		int[] nset = new int[N];
		HashMap<Integer, Integer> mapset = new HashMap<>();
		int sum = 0;

		for (int i = 0; i < N; i++) {
			int k = Integer.parseInt(br.readLine());
			sum += k;
			nset[i] = k;
			if (mapset.containsKey(k)){
				mapset.replace(k, mapset.get(k)+1);
			} else {
				mapset.put(k, 1);
			}
		}

		// 산술평균
		sum = Math.round((float) sum/N);
		sb.append(sum).append("\n");

		// 중앙값
		Arrays.sort(nset);
		int idx = N/2;
		sb.append(nset[idx]).append("\n");

		// 최빈값

		int max = Collections.max(mapset.values());
		List<Integer> li = new ArrayList<>();
		for (int l : mapset.keySet()) {
			if (mapset.get(l) == max){
				li.add(l);
			}
		}

		Collections.sort(li);

		if (li.size()==1) sb.append(li.get(0)).append("\n");
		else sb.append(li.get(1)).append("\n");

		// 범위

		sb.append(nset[N-1] - nset[0]).append("\n");

		System.out.print(sb);

	}
}

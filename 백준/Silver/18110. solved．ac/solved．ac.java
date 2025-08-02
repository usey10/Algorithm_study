import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());

		List<Integer> levels = new ArrayList<>();
		int grade = 0;
		for (int i = 0; i < N; i++) {
			levels.add(Integer.parseInt(br.readLine()));
		}

		Collections.sort(levels);

		int non = (int) Math.round(N * 0.15);

		if (N != 0){
			for (int i = non; i < N-non; i++) {
				grade += levels.get(i);
			}
			grade = Math.round((float)grade / (float) (N-(2*non)));
		} 

		System.out.println(grade);

	}
}

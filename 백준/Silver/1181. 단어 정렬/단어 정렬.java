import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		Set<String> words = new HashSet<String>();
		for (int i=0;i<N;i++) {
			String word = br.readLine();
			words.add(word);
		}
		
		List<String> li = new ArrayList<String>(words);		
		Collections.sort(li);
		Collections.sort(li, (String a, String b) -> a.length() - b.length());
		

		for (String str:li) {
			System.out.println(str);
		}

	}
}
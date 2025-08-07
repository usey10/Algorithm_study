import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String line = br.readLine();
		Map<Character, Integer> counts = new HashMap<>();
		
		for (int i=0;i<line.length();i++) {
			char x = line.charAt(i);
			if (x>=97) {
				x -= 32;
			}
			
			if (counts.containsKey(x)) {
				counts.replace(x, counts.get(x)+1);
			} else {
				counts.put(x, 1);
			}
		}
		
		int max = 0;
		for (int li:counts.values()) {
			if (max < li) max = li;
		}
		
		int cnt = 0;
		char result = ',';
		for (char el:counts.keySet()) {
			if (max == counts.get(el)) {
				result = el;
				cnt++;
			}
		}
		
		if (cnt > 1) {
			System.out.println("?");
		} else {
			System.out.println(result);
		}
		
	}

}
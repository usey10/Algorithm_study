import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] lines = br.readLine().split(" ");
		
		int le = lines.length;
		
		
		for (String li :lines) {
			if (li == "") {le -= 1;}
		}
		
		System.out.println(le);
	}
}
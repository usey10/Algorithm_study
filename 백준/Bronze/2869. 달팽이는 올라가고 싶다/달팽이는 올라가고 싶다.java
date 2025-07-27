import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] lines = br.readLine().split(" ");
		int a = Integer.parseInt(lines[0]);
		int b = Integer.parseInt(lines[1]);
		int v = Integer.parseInt(lines[2]);
		
		int k = (v-a)%(a-b);
		if (k != 0) {
			System.out.println(((v-a)/(a-b))+2);
		} else {
			System.out.println(((v-a)/(a-b))+1);
		}

	}
}
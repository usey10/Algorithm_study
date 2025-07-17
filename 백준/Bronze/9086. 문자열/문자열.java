import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String T = br.readLine();
		for (int i=1;i<=Integer.parseInt(T);i++) {
			String temp = br.readLine();
			int N = temp.length();
			System.out.println(temp.charAt(0)+""+temp.charAt(N-1));
		}

	}
}
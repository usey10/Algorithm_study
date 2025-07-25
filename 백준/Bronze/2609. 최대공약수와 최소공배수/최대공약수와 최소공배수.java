import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;



public class Main {
	// 유클리드 호제법 사용하기.
	static int gcd(int x, int y) {
		while (y !=0) {
			int r = x%y;
			x = y;
			y = r;
		}
		return x;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] line = br.readLine().split(" ");
		
		int a = Integer.parseInt(line[0]);
		int b = Integer.parseInt(line[1]);
		
		int g = gcd(Integer.max(a,b), Integer.min(a,b));
		
		long l = (long) a/g * b;
		
		
		System.out.println(g);
		System.out.println(l);
		
	}
		
}
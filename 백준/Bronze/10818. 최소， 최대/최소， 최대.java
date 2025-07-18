import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String n = br.readLine();
		String[] NSet = br.readLine().split(" ");
		
		int min = 1000000;
		int max = -1000000;		
		
		for (int i=0;i<Integer.parseInt(n);i++) {
			int temp = Integer.parseInt(NSet[i]);
			if (temp>max) {
				max = temp;
			}
			if (temp < min) {
				min = temp;
			}
		}
		System.out.println(min+ " "+ max);
		
	}
}
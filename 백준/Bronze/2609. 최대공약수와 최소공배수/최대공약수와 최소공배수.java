import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] line = br.readLine().split(" ");
		
		int a = Integer.parseInt(line[0]);
		int b = Integer.parseInt(line[1]);
		
		int maxd = 0;
		
		for (int i=Integer.min(a, b);i>=1;i--) {
			if((a%i==0)&&(b%i==0)) {
				maxd = i;
				break;
			}
		}
		
		int mind = maxd;
		
		while ((mind%a!=0)||(mind%b!=0)) {
			mind += maxd;
		}
		
		System.out.println(maxd);
		System.out.println(mind);
		
	}
		
}
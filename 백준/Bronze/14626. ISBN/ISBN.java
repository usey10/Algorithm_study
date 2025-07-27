import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String lines = br.readLine();
		
		int k = 0;
		int sum = 0;
		
		for (int i=0;i<lines.length();i++) {
			if (lines.charAt(i) == '*') {
				k = i;
			} else {
				if(i%2==0) {
					sum += Integer.parseInt(String.valueOf(lines.charAt(i)));
				}else {
					sum += 3 * (Integer.parseInt(String.valueOf(lines.charAt(i))));
				}
			}
		}
		
		sum = sum % 10;
		sum = 10 - sum;
		int result = 0;
		
		if (k%2 ==0) {
			result = sum;
		} else {
			switch (sum) {
			case 3:
			case 6:
			case 9:
				result = sum;
				break;
			case 2:
			case 5:
			case 8:
				result = (sum+10)/3;
				break;
			case 1:
			case 4:
			case 7:
				result = (sum+20)/3;
				break;
			case 0:
				result = 0;
			}
		}
		
		System.out.println(result);
	}
}
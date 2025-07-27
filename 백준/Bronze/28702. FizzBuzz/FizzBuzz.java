import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] lines = new String[3];
		int startNum = 0;

		for(int i=0;i<3;i++) {
			lines[i] = br.readLine();
			if ((!lines[i].contains("Fizz")) && (!lines[i].contains("Buzz"))) {
				startNum = Integer.parseInt(lines[i]) + 3 - i;
				break;
			}
		}
		
		if ((startNum%3==0) && (startNum%5==0)) {
			System.out.println("FizzBuzz");
		} else if (startNum%3 ==0) {
			System.out.println("Fizz");
		} else if (startNum%5 == 0) {
			System.out.println("Buzz");
		} else {
			System.out.println(startNum);
		}
		
	}
}
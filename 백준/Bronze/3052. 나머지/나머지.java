import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
				
		
        boolean[] left = new boolean[42];

		for (int i=0;i<10;i++) {
			String a = br.readLine();
			int A = Integer.parseInt(a);
			left[(A % 42)] = true;
			}
        
        int count = 0;
        for (int i=0;i<left.length;i++){
            if (left[i]){ count += 1; }
        }

		System.out.println(count);
        
		
	}
}
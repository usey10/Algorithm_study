import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
	
	static int person(int floor, int room) {
		if (floor == 0) {
			return room; // 출구 조건
		}
		
		int sum = 0;
		for (int i=0;i<room;i++) {
			sum += person(floor-1, (i+1));
		}
		
		return sum;
		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int i=0;i<T;i++) {
			int k = Integer.parseInt(br.readLine());
			int n = Integer.parseInt(br.readLine());
			
			System.out.println(person(k,n));
		}
	}
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


public class Main {
	
	public static int mincase(String[] chess, int xNum, int yNum) {
		
		char[] wb = {'W','B'};
		int case1 = 0;
		int case2 = 0;
		
		for (int i=xNum;i<xNum+8;i++) {
			for (int j=yNum;j<yNum+8;j++) {
				char check = chess[i].charAt(j);
				
				case1 += (wb[(i+j)%2] == check)? 0:1;
				case2 += (wb[(i+j)%2] == check)? 1:0;
			}
		}
		
		return Integer.min(case1, case2);
	}
	public static void main(String[] arge) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] lines = br.readLine().split(" ");
		int n = Integer.parseInt(lines[0]);
		int m = Integer.parseInt(lines[1]);
		
		
		String[] chess = new String[n];
		int value = Integer.MAX_VALUE;
		
		for (int i=0;i<n;i++) {
			chess[i] = br.readLine();
		}
		
		for (int i=0;i<n-7;i++) {
			for(int j=0;j<m-7;j++) {
				value = Integer.min(mincase(chess, i,j), value);
			}
		}
		
		System.out.println(value);
		

	}
}

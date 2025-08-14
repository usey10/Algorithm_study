import java.util.Arrays;
import java.util.Scanner;
import java.io.FileInputStream;
import java.util.Deque;
import java.util.List;
import java.util.ArrayDeque;
import java.util.ArrayList;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		sc.nextLine();

		for(int tc = 1; tc <= T; tc++)
		{
			String lines = sc.nextLine();
			char[] o = lines.toCharArray();
			
			int cnt = 0;
			int cNum = 0;
			
			// 첫 시작점 찾기
			for (int i=0;i<o.length;i++) {
				if (o[i] == '1') {
					cNum = i;
					cnt++;
					break;
				}
			}
			
			// 이전값 체크 후 count
			char before = o[cNum];
			for (int i=cNum;i<o.length;i++) {
				if (before != o[i]) {
					cnt++;
					before = o[i];
				}
			}
			
			System.out.println("#" + tc + " " + cnt);
		}
	}
	
	
	
}
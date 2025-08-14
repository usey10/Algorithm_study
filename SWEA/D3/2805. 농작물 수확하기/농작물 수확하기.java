import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());
		
		for(int tc = 1; tc <= T; tc++)
		{
			int N = Integer.parseInt(br.readLine());
			
			String[] farm = new String[N];
			
			for (int i=0;i<N;i++) {
				farm[i] = br.readLine();
			}
			
			int r = 0;
			int sumc = 0;
			for (int i=0;i<N;i++) {
				
				for (int j=N/2-sumc;j<=N/2+sumc;j++) {
					r += farm[i].charAt(j) - '0';
				}
				
				if (i < N/2) sumc++;
				else sumc--;
			}
			
			sb.append("#").append(tc).append(" ").append(r).append("\n");
		}
		
		System.out.print(sb.toString());
	}
	
	
	
}
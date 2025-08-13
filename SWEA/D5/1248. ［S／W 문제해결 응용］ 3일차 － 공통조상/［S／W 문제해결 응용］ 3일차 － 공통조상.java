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

		for(int tc = 1; tc <= T; tc++)
		{
			int V = sc.nextInt();
			int E = sc.nextInt();
			
			int x = sc.nextInt();
			int y = sc.nextInt();
			
			int[][] nodes = new int[E][];
			
			// 간선 저장
			for (int i=0;i<E;i++) {
				int p = sc.nextInt();
				int c = sc.nextInt();
				
				int[] node = {p, c};
				
				nodes[i] = node;
			}
			
			// System.out.println(Arrays.deepToString(nodes));
			

			// 이게 sort 가 안되어있다..!
			// parents 를 제대로 찾아오기가 어렵다 배열을 가지고 하면!
			List<Integer> xList = new ArrayList<>();
			List<Integer> yList = new ArrayList<>();
			
			
			int cx = x, cy = y;
			xList.add(cx);
			yList.add(cy);
			while (true) {
				int xcheck = cx;
				int ycheck = cx;
				for (int j=0;j<E;j++) {
					if (nodes[j][1] == cx) {
						cx = nodes[j][0];
						xList.add(cx);
					}
					
					if (nodes[j][1] == cy) {
						cy = nodes[j][0];
						yList.add(cy);
					}
				}
				
				if (xcheck == cx && ycheck == cy) break;
			}
				
			// System.out.println(xList);
			// System.out.println(yList);
			
			int parents = 0;
			
			for (int i=0;i<xList.size();i++) {
				for (int j=0;j<yList.size();j++) {
					// System.out.println(xList.get(i) + ", y  : " + yList.get(j));
					if (xList.get(i).equals(yList.get(j))) {
						parents = xList.get(i);
						// System.out.print(parents);
						break;
					}
				}
				if (parents != 0) break;
			}
			
			// System.out.println(parents);
			
			int cnt = 0;
			Deque<Integer> deque = new ArrayDeque<>();
			deque.add(parents);
			while (!deque.isEmpty()) {
				int k = deque.pop();
				for (int[] li : nodes) {
					if (li[0] == k) {
						cnt++; 
						deque.add(li[1]);
					}
				}
			}
			
			// 마지막 노드 cnt
			cnt++;
			
			System.out.println("#" + tc + " " + parents + " " + cnt);
			

		}
	}
	
}
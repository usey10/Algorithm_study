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
		
		// 배열로 직접 구현해보기 
		for(int tc = 1; tc <= T; tc++)
		{
			StringBuilder sb = new StringBuilder();
			int N = sc.nextInt();
			heap = new int[N+1];
			idx = 0;
			
			for (int i=0;i<N;i++) {
				int cal = sc.nextInt();
				
				if (cal == 1) {
					int x = sc.nextInt();
					heapAdd(x);
				} else {
					sb.append(heapPop()).append(" ");
				}
			}
			
			System.out.println("#" + tc + " " + sb.toString());
		}
	}
	
	public static int idx;
	public static int[] heap;
	public static void heapAdd(int x) {
		int chI = ++idx;
		int pI = chI / 2;
		heap[chI] = x;
		while (chI != 1 && heap[chI] > heap[pI]) {
			int tmp = heap[pI];
			heap[pI] = heap[chI];
			heap[chI] = tmp;
			
			chI = pI;
			pI = chI / 2;
		}
		// System.out.println(Arrays.toString(heap));
	}
	
	public static int heapPop() {
		if (idx == 0) return -1;
		int r = heap[1];
		heap[1] = heap[idx--];
		
		int p=1;
		int ch;
		while (p*2 <= idx) {
			ch = p * 2;
			if (ch+1 <= idx && heap[ch+1] > heap[ch]) {
				ch += 1;
			}
			
			if (heap[p] >= heap[ch]) break; // 정렬을.. 안했어
			
			int tmp = heap[p];
			heap[p] = heap[ch];
			heap[ch] = tmp;
			
			p = ch;
		}
		
		return r;
	}
	
	
}
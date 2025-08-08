

class Solution {
    public int[][] solution(int n) {
        return hanoii(n,1,2,3);
    }
    
    public int[][] hanoii(int n, int a, int b, int c){
        if (n == 2){
            return new int[][] {{a,b}, {a,c}, {b,c}};
        }
        else {
        	
            int[][] answer = new int[(int) (Math.pow(2,n)-1)][];
            int[][] a1 = hanoii(n-1, a, c, b);
            int[][] a2 = hanoii(n-1, b, a, c);
            for (int i=0;i<a1.length;i++) {
            	answer[i] = a1[i];
            }
            int[] k = {a,c};
            answer[a1.length] = k;
            for (int j=0, idx = a1.length+1;j<a2.length;j++) {
            	answer[idx++] = a2[j]; 
            }
            return answer;
        }
    }
}
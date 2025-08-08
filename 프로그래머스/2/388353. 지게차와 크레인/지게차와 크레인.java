import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public int solution(String[] storage, String[] requests) {
    	int n = storage.length;
    	char[][] storageChar = new char[n][];
    	
    	for (int i=0;i<n;i++) {
    		storageChar[i] = storage[i].toCharArray();
    	}
    	
    	for (String li:requests) {
    			char k = li.charAt(0);
    			List<int[]> xy = new ArrayList<>();
    			List<int[]> xy1 = new ArrayList<>();
    			for (int x=0;x<n;x++) {
    				for (int y=0;y<storageChar[x].length;y++) {
    					if (storageChar[x][y] == k) {
    						int sum = 0;
    						sum += (x-1>=0 && storageChar[x-1][y] != '0')? 1:0;
    						sum += (x+1<n && storageChar[x+1][y] != '0')? 1:0;
    						sum += (y-1>=0 && storageChar[x][y-1] != '0')? 1:0;
    						sum += (y+1<storageChar[x].length && storageChar[x][y+1] != '0')? 1:0;
    						if (sum < 4) {
    							int[] tmp = {x,y};
    							xy.add(tmp);
    						}
    						else if (li.length()==2 && sum == 4) {
    							int[] tmp = {x,y};
    							xy1.add(tmp);
    						}
    					}
    				}
    			}
        
    			
    			if (!(xy.isEmpty())) {
    				for (int[] x : xy) {
    					storageChar[x[0]][x[1]] = '0';
    				}
    			}
    			if (!(xy1.isEmpty())) {
    				for (int[] x : xy1) {
                        // int sum = 0;
                        // sum += (x[0]-1>=0 && storageChar[x[0]-1][x[1]] != '0')? 1:0;
                        // sum += (x[0]+1<n && storageChar[x[0]+1][x[1]] != '0')? 1:0;
                        // sum += (x[1]-1>=0 && storageChar[x[0]][x[1]-1] != '0')? 1:0;
                        // sum += (x[1]+1<storageChar[x[0]].length && storageChar[x[0]][x[1]+1] != '0')? 1:0;
                        // if (sum < 4) storageChar[x[0]][x[1]] = '0';
    					// else storageChar[x[0]][x[1]] = '1';
                        storageChar[x[0]][x[1]] = '1';
    				}
    			}
    			
    			
    			for (int x=0;x<n;x++) {
    				for (int y=0;y<storageChar[x].length;y++) {
    					if (storageChar[x][y] == '0') {
    						if (x-1>=0 && storageChar[x-1][y] == '1') storageChar[x-1][y] = '0';
    						if (x+1<n && storageChar[x+1][y] == '1') storageChar[x+1][y] = '0';
    						if (y-1>=0 && storageChar[x][y-1] == '1') storageChar[x][y-1] = '0';
    						if (y+1<storageChar[x].length && storageChar[x][y+1] == '1') storageChar[x][y+1] = '0';
    					}
    				}
    			}
            
                for (int x=0;x<n;x++) {
                        for (int y=0;y<storageChar[x].length;y++) {
                            if (storageChar[x][y] == '1') {
                                if (x-1>=0 && storageChar[x-1][y] == '0') storageChar[x][y] = '0';
                                if (x+1<n && storageChar[x+1][y] == '0') storageChar[x][y] = '0';
                                if (y-1>=0 && storageChar[x][y-1] == '0') storageChar[x][y] = '0';
                                if (y+1<storageChar[x].length && storageChar[x][y+1] == '0') storageChar[x][y] = '0';
                            }
                        }
                    }
            
            
            
               //System.out.println(Arrays.deepToString(storageChar));
    			
    	
    	}
    	
    	int answer = 0;
    	for (int i=0;i<n;i++) {
    		for (int j=0;j<storageChar[i].length;j++) {
    			if (storageChar[i][j] >= 'A' && storageChar[i][j] <= 'Z') {
    				answer += 1;
    			}
    		}
    	}
        return answer;
    }
    
}
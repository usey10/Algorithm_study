import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

class CalAvg{
	int n;
	int[] student;
	int sum;
	
	CalAvg(String line){
		StringTokenizer st = new StringTokenizer(line);
		this.n = Integer.parseInt(st.nextToken());
		this.student = new int[n];
		for(int i=0;i<n;i++) {
			this.student[i] = Integer.parseInt(st.nextToken());
			this.sum += this.student[i];
		}
	}
	
	double sumCal(){
		double result = (double) sum / n;
		return result;
	}
	
	double percent(double avg) {
		int p = 0;
		double onePer = ((double)100 / this.n) * 1000;
		for (int st:student) {
			if(st > avg) {
				p++; 
			}
		}
		return onePer * p;
	}
}

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String C = br.readLine();
		
		for(int i=0;i<Integer.parseInt(C);i++) {
			String temp = br.readLine();
			CalAvg ca = new CalAvg(temp);
			double avg = ca.sumCal();
			double result = ca.percent(avg);
			System.out.printf("%.3f%%\n", result/1000);
		}
	}
}
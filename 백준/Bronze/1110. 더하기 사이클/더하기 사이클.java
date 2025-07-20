import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Cycle{
	int count = 0;
	int first;
	int num;
	
	Cycle(int num){
		this.first = num;
		this.num = num;
	}
	
	int routine() {
		if (num<10) {
			num = (num*10) + num;
			count++;
		} else {
			int ten = num/10;
			int one = num%10;
			int next = (ten+one)%10;
			num = (one*10) + next;
			count++;
		}
		
		while (first != num) {
			if (num<10) {
				num = (num*10) + num;
				count++;
			} else {
				int ten = num/10;
				int one = num%10;
				int next = (ten+one)%10;
				num = (one*10) + next;
				count++;
			}
		}
		
		return count;

	}
}

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		Cycle cy = new Cycle(N);
		System.out.println(cy.routine());
		
	}
}
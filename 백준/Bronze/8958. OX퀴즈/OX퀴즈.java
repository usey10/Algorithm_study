import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Score {
	int currect = 0;
	int before;
	boolean right;
	String quiz;

	Score(String quiz){
		this.quiz = quiz;
	}
	
	int calScore(){
		for (int i=0;i<quiz.length();i++) {
			if (quiz.charAt(i) == 'O' && right) {
				before += 1;
				currect += before;
			} else if (quiz.charAt(i) == 'O') {
				before = 1;
				currect += before;
				right = true;
			} else if (quiz.charAt(i) != 'O' && right) {
				before = 0;
				right = false;
			}
		}
		return currect;
	}
}

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String testCase = br.readLine();
		
		for (int tc=0;tc<Integer.parseInt(testCase);tc++) {
			String quiz = br.readLine();
			Score sc = new Score(quiz);
			int result = sc.calScore();
			System.out.println(result);
		}
		
	}
}
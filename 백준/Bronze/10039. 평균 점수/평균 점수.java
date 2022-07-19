import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int a = 0;
		for(int i=0; i<5; i++) {
			int score = sc.nextInt();
			if(score<40) {
				a += 40;
			} else {
				a += score;
			}
		}
		
		System.out.println(a/5);
	}

}

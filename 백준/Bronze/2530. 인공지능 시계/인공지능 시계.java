import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int d = sc.nextInt();
		
		int time = a*3600+b*60+c+d;
		int h = time/3600;
		int m = (time-h*3600)/60;
		int s = (time-h*3600)%60;
		
		while(h>=24) {
			h -= 24;
		}
		
		System.out.printf("%d %d %d", h, m, s);
		
	}

}

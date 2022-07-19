import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		if(n==1) {
			System.out.println("");
		} else {
			while(n>1) {
				for(int i=2; i<n+1; i++) {
					if(n%i==0) {
						System.out.println(i);
						n /= i;
						break;
					}
				}
			}
		}
		
	}

}

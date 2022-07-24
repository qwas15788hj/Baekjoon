import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		for(int i=1; i<n+1; i++) {
			for(int j=0; j<i; j++) {
				System.out.print("*");
			}
			for(int z=0; z<(n*2)-(i*2); z++) {
				System.out.print(" ");
			}
			for(int k=0; k<i; k++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		for(int i=n-1; i>0; i--) {
			for(int j=0; j<i; j++) {
				System.out.print("*");
			}
			for(int z=0; z<(n*2)-(i*2); z++) {
				System.out.print(" ");
			}
			for(int k=0; k<i; k++) {
				System.out.print("*");
			}
			System.out.println();
		}

	}

}

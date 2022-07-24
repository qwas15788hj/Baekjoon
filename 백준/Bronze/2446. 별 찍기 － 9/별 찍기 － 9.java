import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		for(int i=n; i>0; i--) {
			for(int j=0; j<n-i; j++) {
				System.out.print(" ");
			}
			for(int z=0; z<(i*2)-1; z++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		for(int i=2; i<n+1; i++) {
			for(int j=0; j<n-i; j++) {
				System.out.print(" ");
			}
			for(int z=0; z<(i*2)-1; z++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
	}

}

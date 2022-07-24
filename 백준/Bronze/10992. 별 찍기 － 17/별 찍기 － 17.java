import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		for(int i=0; i<n-1; i++) {
			for(int j=0; j<n-1-i; j++) {
				System.out.print(" ");
			}
			System.out.print("*");
			if(i!=0) {
				for(int z=0; z<(i*2)-1; z++) {
					System.out.print(" ");
				}
				System.out.print("*");
			}
			System.out.println();
		}
		
		for(int i=0; i<(n*2)-1; i++) {
			System.out.print("*");
		}
		
	}

}

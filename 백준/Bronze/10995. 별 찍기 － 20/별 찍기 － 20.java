import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		for(int i=0; i<n; i++) {
			if(i%2==0) {
				for(int j=0; j<(n*2)-1; j++) {
					if(j%2==0) System.out.print("*");
					else System.out.print(" ");
				}
			} else {
				for(int z=0; z<n*2; z++) {
					if(z%2==0) System.out.print(" ");
					else System.out.print("*");
				}
			}
			System.out.println();
		}
		
	}

}

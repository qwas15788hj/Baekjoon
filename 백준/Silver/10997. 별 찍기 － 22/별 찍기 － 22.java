import java.io.InputStreamReader;

import java.io.BufferedReader;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		if(n==1) {
			System.out.println("*");
		}
		else {
			int loop = (4*n-3)/2;
			int cnt = 1;
			
			for(int i=0; i<4*n-3; i++) {
				System.out.print("*");
			}
			System.out.println();
			System.out.println("*");
			for(int i=loop; i>1; i--) {
				if(i%2==0) {
					for(int j=0; j<cnt; j++) {
						System.out.print("* ");
					}
					for(int z=0; z<2*i-1; z++) {
						System.out.print("*");
					}
					for(int k=0; k<cnt-1; k++) {
						System.out.print(" *");
					}
					cnt += 1;
					
				} else {
					for(int j=0; j<cnt; j++) {
						System.out.print("* ");
					}
					for(int z=0; z<2*i-3; z++) {
						System.out.print(" ");
					}
					for(int k=0; k<cnt-1; k++) {
						System.out.print(" *");
					}
				}
				System.out.println();
			}//for
			cnt -= 1;
			
			for(int i=0; i<2; i++) {
				for(int j=0; j<4*n-3; j++) {
					if(j%2==0) {
						System.out.print("*");
					} else {
						System.out.print(" ");
					}
				}
				System.out.println();
			}
			
			for(int i=0; i<2*n-2; i++) {
				if(i%2==0) {
					for(int j=0; j<cnt; j++) {
						System.out.print("* ");
					}
					for(int z=0; z<2*i+1; z++) {
						System.out.print(" ");
					}
					for(int k=0; k<cnt; k++) {
						System.out.print(" *");
					}
					cnt -= 1;
				} else {
					for(int j=0; j<cnt; j++) {
						System.out.print("* ");
					}
					for(int z=0; z<2*i+3; z++) {
						System.out.print("*");
					}
					for(int k=0; k<cnt; k++) {
						System.out.print(" *");
					}
						
				}
				System.out.println();
			}
		}
		

	}

}

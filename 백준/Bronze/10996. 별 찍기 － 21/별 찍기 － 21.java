import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		for(int i=0; i<n*2; i++) {
			if(i%2==0) {
				for(int j=0; j<n; j++) {
					if(j%2==0) System.out.print("*");
					else System.out.print(" ");
				}
			} else {
				for(int z=0; z<n; z++) {
					if(z%2==0) System.out.print(" ");
					else System.out.print("*");
				}
			}
			System.out.println();
		}
		
	}

}

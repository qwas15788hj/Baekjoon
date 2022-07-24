import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		for(int i=0; i<n; i++) {
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
		
	}

}

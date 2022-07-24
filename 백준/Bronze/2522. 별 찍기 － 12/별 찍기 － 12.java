import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		for(int i=1; i<n+1; i++) {
			for(int j=0; j<n-i; j++) {
				System.out.print(" ");
			}
			for(int z=0; z<i; z++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		for(int i=n-1; i>0; i--) {
			for(int j=0; j<n-i; j++) {
				System.out.print(" ");
			}
			for(int z=0; z<i; z++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
	}

}

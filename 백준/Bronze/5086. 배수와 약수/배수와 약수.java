import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			if(a==0 && b==0) break;
			
			if(b%a==0) {
				System.out.println("factor");
			} else if(a%b==0) {
				System.out.println("multiple");
			} else {
				System.out.println("neither");
			}
		}
	}

}

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		
		int answer = 10;
		for(int i=1; i<str.length(); i++) {
			if(str.charAt(i-1) == str.charAt(i)) {
				answer += 5;
			} else {
				answer += 10;
			}
		}
		System.out.println(answer);
		
	}

}

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
		
		int t = Integer.parseInt(br.readLine());
		for(int i=0; i<t; i++) {
			String str = br.readLine();
			StringTokenizer st = new StringTokenizer(str, " ");
			
			double answer = Double.parseDouble(st.nextToken());
			while(st.hasMoreTokens()) {
				String op = st.nextToken();
				if(op.equals("@")) {
					answer *= 3;
				} else if(op.equals("%")) {
					answer += 5;
				} else if(op.equals("#")) {
					answer -= 7;
				}
			}
			System.out.printf("%.2f", answer);
			System.out.println();
		}
	}

}

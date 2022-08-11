import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int[] arr = new int[9];
		int sum = 0;
		for(int i=0; i<9; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			sum += arr[i];
		}
		
		int a = 0;
		int b = 0;
		for(int i=0; i<8; i++) {
			for(int j=i+1; j<9; j++) {
				if(sum-arr[i]-arr[j]==100) {
					a = i;
					b = j;
					break;
				}
			}
		}
		
		for(int i=0; i<9; i++) {
			if(i!=a && i!=b) {
				sb.append(arr[i]);
				sb.append("\n");
			}
		}
		
		System.out.println(sb);

	}//main

}//class

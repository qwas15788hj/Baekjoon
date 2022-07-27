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
		int n = sc.nextInt();
		
		int[] arr = new int[n+1];
		arr[0] = 0;
		arr[1] = 1;
		
		for(int i=2; i<n+1; i++) {
			arr[i] = arr[i-2] + arr[i-1];
		}
		System.out.println(arr[n]);
	}

}

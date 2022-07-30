import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.regex.Pattern;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		StringTokenizer st = new StringTokenizer(str, " ");
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		String str2 = br.readLine();
		StringTokenizer st2 = new StringTokenizer(str2, " ");
		int[] arr = new int[n];
		for(int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st2.nextToken());
		}
		
		int answer = Integer.MIN_VALUE;
		int sum = 0;
		boolean flag = false;
		for(int i=0; i<n-2; i++) { //i는 0~n-2까지만
			for(int j=i+1; j<n-1; j++) { //j는 i+1~n-1
				for(int z=j+1; z<n; z++) { //z는 j+1~n
					sum = arr[i]+arr[j]+arr[z];
					if(sum==m) {
						answer = sum;
						flag = true;
						break;
					}
					if(sum>answer && sum<m) answer = sum; //answer보다 크고 m보다 작으면 갱신
				}
				if(flag==true) break;
			}
			if(flag==true) break;
		}
		System.out.println(answer);
	}

}

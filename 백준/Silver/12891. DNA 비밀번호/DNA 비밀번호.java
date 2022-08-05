import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int count = 0;
	public static void main(String[] args) throws IOException {
			
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int s = Integer.parseInt(st.nextToken());
		int p = Integer.parseInt(st.nextToken());
		// 문자
		String str = br.readLine();
		StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
		int[] arr = new int[4];
		// 조건
		for(int i=0; i<4; i++) {
			arr[i] = Integer.parseInt(st1.nextToken());
		}
		
		int[] darr = new int[4];
		for(int i=0; i<p; i++) {
			if(str.charAt(i)=='A') darr[0]+=1;
			else if(str.charAt(i)=='C') darr[1]+=1;
			else if(str.charAt(i)=='G') darr[2]+=1;
			else if(str.charAt(i)=='T') darr[3]+=1;
			
		}
		if(check(arr, darr)) count+=1;
		
		for(int i=0; i<s-p; i++) {
			if(str.charAt(i)=='A') darr[0]-=1;
			else if(str.charAt(i)=='C') darr[1]-=1;
			else if(str.charAt(i)=='G') darr[2]-=1;
			else darr[3]-=1;
			
			if(str.charAt(p+i)=='A') darr[0]+=1;
			else if(str.charAt(p+i)=='C') darr[1]+=1;
			else if(str.charAt(p+i)=='G') darr[2]+=1;
			else darr[3]+=1;
			
//			System.out.println(Arrays.toString(darr));
			if(check(arr, darr)) count+=1;
			
		}
		System.out.println(count);
		
	}//main
	
	static boolean check(int[] arr, int[] darr) {
		boolean flag = true;
		for(int i=0; i<4; i++) {
			if(darr[i]<arr[i]) {
				flag = false;
				break;
			}
		}
		return flag;
	}
}//class

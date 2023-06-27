import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static int answer;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		
		answer = 0;
		BinarySearch(n, c, r);
		System.out.println(answer);

	}//main
	
	public static void BinarySearch(int n, int x, int y) {
		if(n==0) {
			return;
		}
		
		int len = (int)Math.pow(2, n);
		int half = len/2;
		
		if(x<half && y<half) {
			BinarySearch(n-1, x, y);
			
		} else if(x>=half && y<half) {
			answer += half*half;
			BinarySearch(n-1, x-half, y);
			
		} else if(x<half && y>=half) {
			answer += half*half*2;
			BinarySearch(n-1, x, y-half);
			
		} else if(x>=half && y>=half) {
			answer += half*half*3;
			BinarySearch(n-1, x-half, y-half);
		}
		
		
		
	}//BinarySearch
	

}//class

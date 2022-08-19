import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		int m = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<m; i++) {
			int target = Integer.parseInt(st.nextToken());
			sb.append(upperBound(arr, target, 0, arr.length)-lowerBound(arr, target, 0, arr.length)+" ");
		}
		System.out.println(sb);
		

	}//main
	
	public static int lowerBound(int[] arr, int target, int start, int end) {
		int mid;
		while(start < end) {
			mid = (start+end)/2;
			if(target <= arr[mid]) {
				end = mid;
			} else {
				start = mid+1;
			}
			
		}
		return start;
		
	}
	
	public static int upperBound(int[] arr, int target, int start, int end) {
		int mid;
		while(start < end) {
			mid = (start+end)/2;
			if(target < arr[mid]) {
				end = mid;
			} else {
				start = mid+1;
			}
		}
		return start;
	}

}//class

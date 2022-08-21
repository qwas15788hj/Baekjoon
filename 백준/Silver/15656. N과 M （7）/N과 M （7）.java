import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m;
	static int[] arr;
	static int[] numbers;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n];
		numbers = new int[m];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		
		perm_repeat(0);
		System.out.println(sb);

	}//main
	
	public static void perm_repeat(int cnt) {
		if(cnt==m) {
			for(int i=0; i<numbers.length; i++) {
				sb.append(numbers[i]+" ");
			}
			sb.append("\n");
			
			return;
		}
		
		for(int i=0; i<n; i++) {
			numbers[cnt] = arr[i];
			perm_repeat(cnt+1);
		}
	}
	
}//class

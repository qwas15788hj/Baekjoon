import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n  = Integer.parseInt(st.nextToken());
		int answer = n;
		
		for(int i=0; i<n; i++) {
			String s = br.readLine();
			int prev = 0;
			int[] arr = new int[26];
			
			for(int j=0; j<s.length(); j++) {
				int now = s.charAt(j);
				if(prev != now) {
					if(arr[now-97] == 0) {
						arr[now-97]++;
						prev = now;
					} else {
						answer--;
						break;
					}
				}
			}
		}
		System.out.println(answer);
		
	}

}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static int n;
	static int[] weight;
	static int[] store;
	static boolean[] select;
	static int answer;
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<t+1; tc++) {
			n = Integer.parseInt(br.readLine());
			weight = new int[n];
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<n; i++) {
				weight[i] = Integer.parseInt(st.nextToken());
			}
			
			store = new int[n];
			select = new boolean[n];
			answer = 0;
			perm(0);
			
			sb.append("#"+tc+" "+answer).append("\n");
			
		}//for(test_case)
		
		System.out.println(sb);
		
	}//main
	
	public static void perm(int cnt) {
		if(cnt==n) {
			Subset(0, 0, 0);
			return;
		}
		
		for(int i=0; i<n; i++) {
			if(select[i]) continue;
			
			select[i] = true;
			store[cnt] = weight[i];
			perm(cnt+1);
			select[i] = false;
		}
		
	}//perm
	
	public static void Subset(int idx, int left, int right) {
		if(right > left) return;
		
		if(idx==n) {
			if(left >= right) {
				answer += 1;
				return;
			}
			return;
		}
		
		Subset(idx+1, left+store[idx], right);
		Subset(idx+1, left, right+store[idx]);
		
	}
	
	
}//class

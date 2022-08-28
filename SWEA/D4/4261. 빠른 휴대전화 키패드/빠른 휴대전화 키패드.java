import java.awt.RenderingHints.Key;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static String s;
	static int n, answer;
	static String[] KeyPad = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

	static String[] arr;
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<t+1; tc++) {
			st = new StringTokenizer(br.readLine());
			s = st.nextToken();
			n = Integer.parseInt(st.nextToken());
			arr = new String[n];
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<n; i++) {
				arr[i] = st.nextToken();
			}
			
			answer = 0;
			for(int i=0; i<n; i++) { //n개 단어 수 만큼 돌리기
				boolean flag = true;
				if(arr[i].length() != s.length()) {
					flag = false;
					continue;
				}
				
				for(int j=0; j<arr[i].length(); j++) {
					String arrStr = arr[i].charAt(j)+""; //해당 배열의 j번째 인덱스 값
					int idx = Integer.parseInt(s.charAt(j)+""); //키패드 인덱스
					if(!KeyPad[idx].contains(arrStr)) {
						flag = false;
						break;
					}
				}
				
				if(flag) answer += 1;
				
			}
			
			sb.append("#"+tc+" "+answer).append("\n");
			
			
		}//for(test_case)
		
		System.out.println(sb);
		
	}//main
	
}//class

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static int count(String[][] arr, int n) {
		int max = 0;
		int count = 0;
		//가로마다 같은 색
		for(int i=0; i<n; i++) {
			count = 1;
			for(int j=0; j<n-1; j++) {
				if(arr[i][j].equals(arr[i][j+1])) count+=1;
				else count=1;
				max = Math.max(max, count);
			}
		}
		
		//세로마다 같은 색
		for(int i=0; i<n; i++) {
			count = 1;
			for(int j=0; j<n-1; j++) {
				if(arr[j][i].equals(arr[j+1][i])) count+=1;
				else count=1;
				max = Math.max(max, count);
			}
		}
		
		return max;
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String[][] arr = new String[n][n];
		for(int i=0; i<n; i++) {
			String str = br.readLine();
			for(int j=0; j<n; j++) {
				arr[i][j] = Character.toString(str.charAt(j));
			}
		} //입력
		
		
		int answer = 0;
		int cnt = 0;
		String tmp = "";
		//가로로 바꾸기
		for(int i=0; i<n; i++) {
			for(int j=0; j<n-1; j++) {
				tmp = arr[i][j];
				arr[i][j] = arr[i][j+1];
				arr[i][j+1] = tmp;
				
				cnt = count(arr, n);
				answer = Math.max(answer, cnt);
				
				tmp = arr[i][j];
				arr[i][j] = arr[i][j+1];
				arr[i][j+1] = tmp;
				
			}
		}
		
		//세로로 바꾸기
		for(int i=0; i<n; i++) {
			for(int j=0; j<n-1; j++) {
				tmp = arr[j][i];
				arr[j][i] = arr[j+1][i];
				arr[j+1][i] = tmp;
				
				cnt = count(arr, n);
				answer = Math.max(answer, cnt);
				
				tmp = arr[j][i];
				arr[j][i] = arr[j+1][i];
				arr[j+1][i] = tmp;
			}
		}
		
		System.out.println(answer);

	}//main

}//class
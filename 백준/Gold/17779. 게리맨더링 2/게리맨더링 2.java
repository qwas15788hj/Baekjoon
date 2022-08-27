import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int n;
	static int[][] arr;
	static int answer;
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		n = Integer.parseInt(br.readLine());
		arr = new int[n][n];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		answer = Integer.MAX_VALUE;
		for(int x=0; x<n; x++) {
			for(int y=0; y<n; y++) {
				for(int d1=1; d1<n; d1++) {
					for(int d2=1; d2<n; d2++) {
						if(x+d1+d2<n && y-d1>=0 && y>y-d1 && y+d2<n) {
							gerrymandering(x, y, d1, d2);
						}
					}
				}
			}
		}
		
		System.out.println(answer);

	}//main
	
	public static void gerrymandering(int x, int y, int d1, int d2) {
		int[][] SubArr = new int[n][n];
		int[] person = new int[5]; //선거구별 사람 채우기
		
		for(int i=0; i<=d1; i++) { //경계선1
			SubArr[x+i][y-i] = 5;
		}
		for(int i=0; i<=d2; i++) { //경계선2
			SubArr[x+i][y+i] = 5;
		}
		for(int i=0; i<=d2; i++) { //경계선3
			SubArr[x+d1+i][y-d1+i] = 5;
		}
		for(int i=0; i<=d1; i++) { //경계선4
			SubArr[x+d2+i][y+d2-i] = 5;
		}
		
		//5선거구 채우기
		int start = -1;
		int end = -1;
		for(int i=0; i<n; i++) {
			start = -1;
			end = -1;
			for(int j=0; j<n; j++) {
				if(SubArr[i][j]==5 && start==-1) start=j;
				else if(SubArr[i][j]==5 && start!=-1) end=j;
			}
			
			for(int k=start+1; k<end; k++) {
				SubArr[i][k] = 5;
			}
		}
		
		
		//1선거구 채우기
		for(int i=0; i<x+d1; i++) {
			for(int j=y; j>=0; j--) {
				if(SubArr[i][j]==0) SubArr[i][j] = 1;
			}
		}
		
		//2선거구 채우기
		for(int i=0; i<=x+d2; i++) {
			for(int j=y+1; j<n; j++) {
				if(SubArr[i][j]==0) SubArr[i][j] = 2;
			}
		}
		
		//3선거구 채우기
		for(int i=x+d1; i<n; i++) {
			for(int j=0; j<y-d1+d2; j++) {
				if(SubArr[i][j]==0) SubArr[i][j] = 3;
			}
		}
		
		//4선거구 채우기
		for(int i=x+d2; i<n; i++) {
			for(int j=y-d1+d2; j<n; j++) {
				if(SubArr[i][j]==0) SubArr[i][j] = 4;
			}
		}
		
		
		//선거구 채우기
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				person[SubArr[i][j]-1] += arr[i][j];
			}
		}
		
		Arrays.sort(person);
		answer = Math.min(answer, person[4]-person[0]);
		
	}
	
	

}//class

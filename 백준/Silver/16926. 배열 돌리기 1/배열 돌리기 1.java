import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m, k, turn;
	static int[][] arr;
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int count = 0;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		turn = (n+1)/2; //돌리면 열 개수
		
		for(int i=0; i<k; i++) {
			arr = turn(arr);
		}
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				sb.append(arr[i][j]+" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);

	}//main
	
	private static int[][] turn(int[][] arr) {
		int[][] tArr = new int[n][m];
		for(int t=0; t<turn; t++) {
			int x = t;
			int y = t;
			for(int i=0; i<4; i++) {
				while(true) {
					int nx = x+dx[i];
					int ny = y+dy[i];
					if(nx>=t && nx<n-t && ny>=t && ny<m-t) {
						tArr[nx][ny] = arr[x][y];
						x = nx;
						y = ny;
					} else {
						break;
					}
					
				}
			}
		}
		return tArr;
		
	}//turn

}//class

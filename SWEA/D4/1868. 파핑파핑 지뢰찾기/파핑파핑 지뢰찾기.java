import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution {
	
	static int n;
	static int[][] arr;
	static boolean[][] visited;
	static int[] dx = {-1, 1, 0, 0, -1, -1, 1, 1};
	static int[] dy = {0, 0, -1, 1, -1, 1, -1, 1};
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<t+1; tc++) {
			n = Integer.parseInt(br.readLine());
			arr = new int[n][n];
			for(int i=0; i<n; i++) {
				String str = br.readLine();
				for(int j=0; j<n; j++) {
					if(str.charAt(j)=='*') arr[i][j]=-1;
				}
			} //배열 입력
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					if(arr[i][j]==0) {
						int count = 0;
						for(int k=0; k<8; k++) {
							int nx = i+dx[k];
							int ny = j+dy[k];
							if(nx>=0 && nx<n && ny>=0 && ny<n && arr[nx][ny]==-1) {
								count += 1;
							}
						}
						arr[i][j] = count;
					}
				}
			} //배열 숫자 채우기
			
			
			int answer = 0;
			visited = new boolean[n][n];
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					if(arr[i][j]==0 && !visited[i][j]) { //0이고, 방문 안했으면 주변 돌아야해서
						dfs(i, j); //dfs
						answer += 1;
					}
				}
			}
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					if(arr[i][j]>0 && !visited[i][j]) {
						visited[i][j] = true;
						answer += 1;
					}
				}
			}
			
			sb.append("#"+tc+" "+answer).append("\n");
			
		}//for(test_case)
		
		System.out.println(sb);
		
	}//main
	
	public static void dfs(int x, int y) {
		visited[x][y] = true;
		for(int i=0; i<8; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			if(nx>=0 && nx<n && ny>=0 && ny<n && arr[nx][ny]==0 && !visited[nx][ny]) {
				dfs(nx, ny);
			} else if(nx>=0 && nx<n && ny>=0 && ny<n && arr[nx][ny]>0 && !visited[nx][ny]) {
				visited[nx][ny] = true;
			}
		}
		
	}
	
}//class

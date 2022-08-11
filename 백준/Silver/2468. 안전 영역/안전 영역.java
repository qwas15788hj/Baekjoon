import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int n, min, max;
	static int[][] arr;
	static boolean[][] visited;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int answer;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		arr = new int[n][n];
		min = Integer.MAX_VALUE;
		max = 0;
		for(int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j=0; j<n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if(arr[i][j] > max) max = arr[i][j];
				if(arr[i][j] < min) min = arr[i][j];
			}
		}
		
		answer = 1;
		for(int k=min; k<max; k++) {
			int count = 0;
			visited = new boolean[n][n];
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					if(arr[i][j]>k && !(visited[i][j])) {
						dfs(i, j, k);
						count += 1;
					}
				}
			}
			answer = Math.max(answer, count);
		}
		System.out.println(answer);
		
	}//main
	
	public static void dfs(int x, int y, int k) {
		visited[x][y] = true;
		for(int i=0; i<4; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			if(nx>=0 && nx<n && ny>=0 && ny<n) {
				if(arr[nx][ny] > k && !(visited[nx][ny])) {
					dfs(nx, ny, k);
				}
			}
		}
		
	}//dfs
	

}//class

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m;
	static int[][] arr;
	static boolean[][] visited;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int ice, time;
	static boolean flag;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		} //배열 입력 완료
		
		
		time = 0;
		flag = false;
		while(true) {
			
			melt();
//			for(int i=0; i<n; i++) {
//				System.out.println(Arrays.toString(arr[i]));
//			}
			
			ice = 0;
			visited = new boolean[n][m];
			for(int i=0; i<n; i++) {
				for(int j=0; j<m; j++) {
					if(arr[i][j]!=0 && !(visited[i][j])) {
						dfs(i, j);
						ice += 1;
					}
				}
			}
			
//			System.out.println(ice);
			
			time += 1;
			if(ice==0) {
				flag = false;
				break;
			}
			if(ice>1) {
				flag = true;
				break;
			}
			
			
		}
		
		if(flag) System.out.println(time);
		else System.out.println(0);
		
		
	}//main
	
	public static void melt() {
		int[][] SubArr = new int[n][m];
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(arr[i][j]!=0) {
					int count = 0;
					for(int k=0; k<4; k++) {
						int nx = i+dx[k];
						int ny = j+dy[k];
						if(nx>=0 && nx<n && ny>=0 && ny<m && arr[nx][ny]==0) {
							count += 1;
						}
					} //4방향 탐색
					SubArr[i][j] = Math.max(arr[i][j]-count, 0);
					
				} //해당 배열이 0이 아닐경우(빙산 있다면)
				
			} //가로 for
		} //세로 for
		
		arr = SubArr;
		
	} //melt
	
	public static void dfs(int x, int y) {
		visited[x][y] = true;
		for(int i=0; i<4; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			if(nx>=0 && nx<n && ny>=0 && ny<m) {
				if(arr[nx][ny]!=0 && !(visited[nx][ny])) {
					dfs(nx, ny);
				}
			}
		}
	}
	

}//class

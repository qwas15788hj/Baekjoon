import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int[][] arr;
	static int n, m;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int answer = Integer.MIN_VALUE;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		} //입력
		
		
		dfs(0);
		
		System.out.println(answer);
		
		
	}//main
	
	public static void dfs(int cnt) { //벽 설치
		
		if(cnt==3) {
			bfs();
			return;
		}
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(arr[i][j]==0) { //현재 위치가 빈칸이라면
					arr[i][j] = 1; //벽 설치
					dfs(cnt+1);
					arr[i][j] = 0;
				}
			}
		}
		
	}//dfs
	
	public static void bfs() {
		Queue<int[]> queue = new LinkedList<>();
		for(int i=0; i<n; i++) { //맵을 탐색하면서
			for(int j=0; j<m; j++) {
				if(arr[i][j]==2) { //바이러스 발견하면
					queue.add(new int[] {i, j}); //큐에 추가
				}
			}
		}
		
		int[][] SubArr = new int[n][m]; //큐를 돌기 위한 새로운 배열 생성
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				SubArr[i][j] = arr[i][j];
			}
		}
		
		while(!queue.isEmpty()) {
			int size = queue.size();
			for(int i=0; i<size; i++) {
				int[] temp = queue.poll();
				int x = temp[0];
				int y = temp[1];
				for(int j=0; j<4; j++) { //4방향 탐색
					int nx = x+dx[j];
					int ny = y+dy[j];
					//해당 위치가 범위 내에 존재하고 빈 칸이라면
					if(nx>=0 && nx<n && ny>=0 && ny<m && SubArr[nx][ny]==0) {
						SubArr[nx][ny] = 2; //바이러스 퍼트리고
						queue.add(new int[] {nx, ny}); //큐에 추가
					}
				}
			}
			
		}//while_queue
		
		//안전 영역 탐색
		int count = 0;
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(SubArr[i][j]==0) {
					count += 1;
				}
			}
		}
		
		answer = Math.max(answer, count);
		
	}//bfs
	
	
}//class

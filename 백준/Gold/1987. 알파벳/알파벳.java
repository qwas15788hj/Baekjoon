import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

import javax.swing.InputMap;

public class Main {
	
	static int r, c;
	static int[][] arr;
	static boolean[] visited = new boolean[26];
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int answer;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		arr = new int[r][c];
		for(int i=0; i<r; i++) {
			String str = br.readLine();
			for(int j=0; j<c; j++) {
				arr[i][j] = str.charAt(j)-'A';
			}
		}//입력 완료
		
		answer = 0;
		dfs(0, 0, 1);
		System.out.println(answer);
		

	}//main
	
	public static void dfs(int x, int y, int count) {
		visited[arr[x][y]] = true;
		answer = Math.max(answer, count); //처음 방문한 곳이라면 정답 계속 갱신
		
		for(int i=0; i<4; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			if(nx>=0 && nx<r && ny>=0 && ny<c) { //범위 안에 있고
				if(!(visited[arr[nx][ny]])) { //방문하지 않았다면
					dfs(nx, ny, count+1); //계속 들어감
					visited[arr[nx][ny]] = false; //방문이 끝났다면 초기화
				}
			}
			
		}//for(4방향)
		
	}//dfs
	

}//class

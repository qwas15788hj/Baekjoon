import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int n; //길이
	static char[][] arr; //배열 생성
	static boolean[][] visited; //방문 처리
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1}; // ==> 상하좌우
	static int count1, count2; //일반, 적록색약
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		arr = new char[n][n];
		for(int i=0; i<n; i++) {
			String str = br.readLine();
			for(int j=0; j<n; j++) {
				arr[i][j] = str.charAt(j);
			}
		} //배열 입력 완료
		
		count1 = 0;
		visited = new boolean[n][n];
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(!(visited[i][j])) { //방문하지 않았을 경우
					dfs(i, j, arr[i][j]); //인덱스 값과, 인덱스 값의 char dfs돌리기
					count1 += 1;
				}
			}
		}
		
		//적록색약 값 구하기 위해 배열 값 변경
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(arr[i][j]=='G') arr[i][j]='R';
			}
		}
		
		count2 = 0;
		visited = new boolean[n][n];
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(!(visited[i][j])) {
					dfs(i, j, arr[i][j]);
					count2 += 1;
				}
			}
		}
		
		System.out.println(count1+" "+count2);
		
		
	}//main
	
	public static void dfs(int x, int y, char c) {
		visited[x][y] = true;
		for(int i=0; i<4; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			if(nx>=0 && nx<n && ny>=0 && ny<n && arr[nx][ny]==c && !(visited[nx][ny])) { //범위 내에 있고, 넘어온 글씨와 같고, 방문 하지 않았을 경우
				dfs(nx, ny, c); //dfs돌리기
			}
		}
		
	}
	
	

}//class

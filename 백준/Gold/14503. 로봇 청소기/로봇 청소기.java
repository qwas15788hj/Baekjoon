import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m;
	static int[][] arr;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, 1, 0, -1}; //북동남서
	static int answer;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		int direction = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		answer = 0;
		clean(r, c, direction);
		
		System.out.println(answer);
		
	}//main
	
	public static void clean(int x, int y, int dir) {
		
		//1. 현재 위치 청소
		if(arr[x][y]==0) {
			arr[x][y] = 2;
			answer += 1;
		}
		
		boolean flag = false;
		for(int i=0; i<4; i++) { //4방향 탐색
			int next_dir = (dir+3)%4; //왼쪽 방향
			int next_x = x+dx[next_dir]; //왼쪽 방향 세로 값
			int next_y = y+dy[next_dir]; //왼쪽 방향 가로 값
			if(next_x>=0 && next_x<n && next_y>=0 && next_y<m) { //왼쪽 방향이 범위에 있고
				if(arr[next_x][next_y]==0) { //왼쪽 방향이 청소할 수 있다면
					clean(next_x, next_y, next_dir); //청소하러 가자
					flag = true;
					break;
				}
			}
			dir = (dir+3)%4; //방향만 변경
		}
		
		//4방향 모두 없으면
		if(!flag) {
			int next_dir = (dir+2)%4; //그대로 뒤로 이동하기 위한 방향 설정
			int next_x = x+dx[next_dir];
			int next_y = y+dy[next_dir];
			if(next_x>=0 && next_x<n && next_y>=0 && next_y<m) { //뒤방향이 범위 안에 있고
				if(arr[next_x][next_y]!=1) { //벽이 아니면
					clean(next_x, next_y, dir); //청소하러 가자
				}
			} else { //범위 벗어나면
				return; //끝
			}
		}
		
	}

}//class

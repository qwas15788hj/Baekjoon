import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m, r, answer;
	static int[][] arr;
	static int select[] = new int[3];
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		arr = new int[n+1][m];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		} //입력 받기
		
		answer = 0;
		comb(0, 0);
		System.out.println(answer);
		
	}//main
	
	public static void comb(int count, int start) { //궁수 위치 구하기(조합)
		if(count==3) {
			int[][] gameMap = new int[arr.length][arr[0].length];
			for(int i=0; i<gameMap.length; i++) {
				System.arraycopy(arr[i], 0, gameMap[i], 0, arr[0].length);
			} //새로운 게임맵 깊은 복사
			
			shoot(gameMap);
			return;
		}
		
		for(int i=start; i<m; i++) {
			select[count] = i;
			comb(count+1, i+1);
		}
	}//comb
	
	
	public static void shoot(int[][] gameMap) {
		int count = 0; //몇마리 제거?
		for(int i=0; i<3; i++) {
			gameMap[n][select[i]] = 2;
		} //맵에 궁수 배치
		
		while(check(gameMap)) {
			int[] Monster_x = new int[3]; //가로
			int[] Monster_y = new int[3]; //세로
			int[] Monster_dist = new int[3]; //몬스터와의 거리
			for(int k=0; k<3; k++) {
				int x = select[k]; //가로걸이
				int y = n; //세로걸이
				int dx = Integer.MAX_VALUE/2-1; //가로, 적과의 가로 길이
				int dy = Integer.MAX_VALUE/2-1; //세로, 적과의 세로 길이
				for(int i=0; i<m; i++) {
					for(int j=0; j<n+1; j++) {
						if(gameMap[j][i]==1) { //적을 만나면
							int nx = Math.abs(x-i); //적과의 가로 길이
							int ny = Math.abs(y-j); //적과의 세로 길이
							if(dx+dy > nx+ny) { //거리가 가깝다면
								dx = nx; //갱신
								dy = ny; //갱신
								Monster_x[k] = i; //몬스터 x좌표(가로)
								Monster_y[k] = j; //몬스터 y좌표(세로)
							} //거리가 짧다면 갱신
						}
					}
				}
				Monster_dist[k] = dx+dy; //몬스터와의 거리
			}
			
			for(int i=0; i<3; i++) {
				if(Monster_dist[i] <= r) {
					if(gameMap[Monster_y[i]][Monster_x[i]]==1) {
						gameMap[Monster_y[i]][Monster_x[i]] = 0;
						count += 1;
					}
				}
			} //몬스터가 거리에 있다면 제거!
			
			for(int i=n-1; i>=0; i--) { //맨 밑부터 몬스터 좌표 이동
				for(int j=m-1; j>=0; j--) {
					if(gameMap[i][j]==1) {
						if(i+1 < n) {
							gameMap[i+1][j] = 1;
						}
						gameMap[i][j] = 0;
					}
				}
			} //몬스터 이동
			
		}//while
		
		answer = Math.max(answer, count);
		
	}//shoot
	
	public static boolean check(int[][] gameMap) { //맵에 몬스터가 있는지 체크
		boolean flag = false;
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(gameMap[i][j]==1) {
					flag = true;
				}
			}
		}
		return flag;
	}
	

}//class
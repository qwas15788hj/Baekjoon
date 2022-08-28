import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static int h, w;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, 1, 0, -1}; //==> 상우하좌
	static char[][] arr;
	static String command;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int t = Integer.parseInt(br.readLine());
		int x = 0;
		int y = 0;
		int dir = 0;
		for(int tc=1; tc<t+1; tc++) {
			st = new StringTokenizer(br.readLine());
			h = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			arr = new char[h][w];
			for(int i=0; i<h; i++) {
				String str = br.readLine();
				for(int j=0; j<w; j++) {
					arr[i][j] = str.charAt(j);
					if(arr[i][j]=='^') {
						x = i;
						y = j;
						dir = 0;
					} else if(arr[i][j]=='>') {
						x = i;
						y = j;
						dir = 1;
					} else if(arr[i][j]=='v') {
						x = i;
						y = j;
						dir = 2;
					} else if(arr[i][j]=='<') {
						x = i;
						y = j;
						dir = 3;
					}
				}
			}
			
			int n = Integer.parseInt(br.readLine());
			command = br.readLine();
			
			tank(x, y, dir, 0);
			
			sb.append("#"+tc+" ");
			for(int i=0; i<h; i++) {
				for(int j=0; j<w; j++) {
					sb.append(arr[i][j]);
				}
				sb.append("\n");
			}
			
		}//for(test_case)
		
		System.out.println(sb);
		
	}//main
	
	public static void tank(int x, int y, int dir, int cnt) {
		
		if(cnt==command.length()) return;
		
//		for(int i=0; i<h; i++) {
//			System.out.println(Arrays.toString(arr[i]));
//		}
//		System.out.println();
//		System.out.println("count+command: >>"+cnt+"  "+ command.charAt(cnt));
		
		char cmd = command.charAt(cnt);
		
		if(cmd=='U') {
			dir = 0;
			int nx = x+dx[dir];
			int ny = y+dy[dir];
			if(nx>=0 && nx<h && ny>=0 && ny<w) { //범위 안에 있고
				if(arr[nx][ny]=='.') { //땅이면
					arr[nx][ny] = '^'; //그 땅에서 위보고
					arr[x][y] = '.'; //온 곳 '.'으로 바꿈
					tank(nx, ny, dir, cnt+1); //갈 수 있다.
				} else { //범위 안에 있지만 땅이 아니면
					arr[x][y] = '^'; //지금 위치에서 방향만 바꿈
					tank(x, y, dir, cnt+1); //갈 수 없다.
				}
			} else { //범위 안에 없으면
				arr[x][y] = '^';
				tank(x, y, dir, cnt+1);
			}
			
		} else if(cmd=='D') {
			dir = 2;
			int nx = x+dx[dir];
			int ny = y+dy[dir];
			if(nx>=0 && nx<h && ny>=0 && ny<w) { //범위 안에 있고
				if(arr[nx][ny]=='.') { //땅이면
					arr[nx][ny] = 'v';
					arr[x][y] = '.';
					tank(nx, ny, dir, cnt+1); //갈 수 있다.
				} else { //범위 안에 있지만 땅이 아니면
					arr[x][y] = 'v';
					tank(x, y, dir, cnt+1); //갈 수 없다.
				}
			} else { //범위 안에 없으면
				arr[x][y] = 'v';
				tank(x, y, dir, cnt+1);
			}
			
		} else if(cmd=='L') {
			dir = 3;
			int nx = x+dx[dir];
			int ny = y+dy[dir];
			if(nx>=0 && nx<h && ny>=0 && ny<w) { //범위 안에 있고
				if(arr[nx][ny]=='.') { //땅이면
					arr[nx][ny] = '<';
					arr[x][y] = '.';
					tank(nx, ny, dir, cnt+1); //갈 수 있다.
				} else { //범위 안에 있지만 땅이 아니면
					arr[x][y] = '<';
					tank(x, y, dir, cnt+1); //갈 수 없다.
				}
			} else { //범위 안에 없으면
				arr[x][y] = '<';
				tank(x, y, dir, cnt+1);
			}
			
		} else if(cmd=='R') {
			dir = 1;
			int nx = x+dx[dir];
			int ny = y+dy[dir];
			if(nx>=0 && nx<h && ny>=0 && ny<w) { //범위 안에 있고
				if(arr[nx][ny]=='.') { //땅이면
					arr[nx][ny] = '>';
					arr[x][y] = '.';
					tank(nx, ny, dir, cnt+1); //갈 수 있다.
				} else { //범위 안에 있지만 땅이 아니면
					arr[x][y] = '>';
					tank(x, y, dir, cnt+1); //갈 수 없다.
				}
			} else { //범위 안에 없으면
				arr[x][y] = '>';
				tank(x, y, dir, cnt+1);
			}
			
		} else if(cmd=='S') {
			int nx = x;
			int ny = y;
			while(true) {
				nx += dx[dir];
				ny += dy[dir];
				if(nx>=0 && nx<h && ny>=0 && ny<w) { //범위 안에 있고
					if(arr[nx][ny]=='*') { //벽돌이면 깨고 멈춤
						arr[nx][ny] = '.';
						break;
					} else if(arr[nx][ny]=='#') { //강철이면 멈춤
						break;
					}			
				} else { //범위에 벗어나면 멈춤
					break;
				}
			
			}
			
			tank(x, y, dir, cnt+1);
			
		}
		
		
	}
	
	
}//class

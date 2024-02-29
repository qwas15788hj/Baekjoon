import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int k, w, h;
	static int[][] arr;
	static boolean[][][] visited;
	static int result = Integer.MAX_VALUE;
	static int[] dx = {-1, 1, 0, 0, -2, -2, -1, -1, 1, 1, 2, 2};
	static int[] dy = {0, 0, -1, 1, -1, 1, -2, 2, -2, 2, -1, 1};
	static int a=0;
	static int b=0;
	public static class Monkey {
		int r, c; //높이, 가로
		int k; //점프
		int cnt; //움직인횟수
		
		public Monkey(int r, int c, int k, int cnt) {
			this.r = r;
			this.c = c;
			this.k = k;
			this.cnt = cnt;
		}
		
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		k = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		w = Integer.parseInt(st.nextToken());
		h = Integer.parseInt(st.nextToken());
		
		arr = new int[h][w];
		visited = new boolean[h][w][31];
		
		for(int i=0; i<h; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<w; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		bfs();
		if(result==Integer.MAX_VALUE) {
			result = -1;
		}
		
		System.out.println(result);
	}//main
	
	public static void bfs() {
		Queue<Monkey> queue = new LinkedList<>();
		queue.offer(new Monkey(0, 0, 0, 0));
		visited[0][0][0] = true;
		
		Monkey m;
		while(!queue.isEmpty()) {
			m = queue.poll();
			
			if(m.r==h-1 && m.c==w-1) { //끝 도달 시 종료
				result = Math.min(result, m.cnt);
			}
			
			int dir = 12;
			if(m.k >= k) {
				dir = 4;
			}
			
			for(int i=0; i<dir; i++) {
				int nr = m.r+dx[i];
				int nc = m.c+dy[i];
				int nk = m.k;
				if(i>=4) { //점프시
					nk += 1; //점프카운트
				}
				
				if(nr>=0 && nr<h && nc>=0 && nc<w && !visited[nr][nc][nk] && arr[nr][nc]!=1) {
					visited[nr][nc][nk] = true;
					queue.offer(new Monkey(nr, nc, nk, m.cnt+1));
				}
				
			}
			
		}
		
	}
	
	
}//class

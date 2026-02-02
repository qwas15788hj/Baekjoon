import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int m, n;
	static int[][] arr;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static ArrayList<int[]> start;
	static int answer;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		start = new ArrayList<>();
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if(arr[i][j]==1) {
					start.add(new int[] {i, j});
				}
			}
		}
		
		answer = 0;
		bfs(start);
		
		if(check()) System.out.println(answer-1);
		else System.out.println(-1);
		
	}//main
	
	public static void bfs(ArrayList<int[]> start) {
		Queue<int[]> queue = new LinkedList<>();
		for(int i=0; i<start.size(); i++) {
			queue.offer(start.get(i));
		} //큐에 넣기
		
		while(!queue.isEmpty()) {
			int size = queue.size();
			for(int i=0; i<size; i++) {
				int[] temp = queue.poll();
				int x = temp[0];
				int y = temp[1];
				for(int j=0; j<4; j++) {
					int nx = x+dx[j];
					int ny = y+dy[j];
					if(nx>=0 && nx<n && ny>=0 && ny<m && arr[nx][ny]==0) {
						arr[nx][ny] = 1;
						queue.offer(new int[] {nx, ny});
					}
				}
			}
			
			answer += 1;
			
		}
		
	}//bfs
	
	public static boolean check() {
		boolean flag = true;
		a:
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(arr[i][j]==0) {
					flag = false;
					break a;
				}
			}
		}
		return flag;
	}
	
}//class

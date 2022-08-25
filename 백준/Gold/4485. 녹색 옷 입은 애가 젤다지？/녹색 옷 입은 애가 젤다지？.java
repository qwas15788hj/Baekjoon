import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static class Edge implements Comparable<Edge> { //우선순위 큐를 위한 클래스 생성, 정렬
		int x, y, cost;

		public Edge(int x, int y, int cost) {
			this.x = x;
			this.y = y;
			this.cost = cost;
		}

		@Override
		public int compareTo(Edge o) {
			return this.cost-o.cost;
		}
		
	} //Edge class
	
	static int n; //크기
	static int[][] arr; //맵 배열
	static int[][] distance; //거리
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int tc = 1;
		while(true) {
			n = Integer.parseInt(br.readLine());
			if(n==0) break;
			
			arr = new int[n][n];
			for(int i=0; i<n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<n; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			} //배열 입력 완료
			
			distance = new int[n][n];
			for(int i=0; i<n; i++) {
				Arrays.fill(distance[i], Integer.MAX_VALUE);
			} //거리 MAX로 초기화
			distance[0][0] = arr[0][0]; //시작 지점 갱신
			
			PriorityQueue<Edge> queue = new PriorityQueue<>();
			queue.offer(new Edge(0, 0, distance[0][0])); //우선순위 큐에 시작점 넣기
			while(!queue.isEmpty()) {
				Edge edge = queue.poll();
				for(int i=0; i<4; i++) {
					int nx = edge.x+dx[i]; //다음 위치 세로
					int ny = edge.y+dy[i]; //다음 위치 가로
					if(nx>=0 && nx<n && ny>=0 && ny<n) { //범위 내에 있고
						if(distance[nx][ny] > distance[edge.x][edge.y]+arr[nx][ny]) { //다음 위치 거리가 현재 거리+다음거리 보다 클 경우
							distance[nx][ny] = distance[edge.x][edge.y]+arr[nx][ny]; //다음 위치 거리 갱신
							queue.offer(new Edge(nx, ny, distance[nx][ny])); //다음 위치와 다음위치 거리 큐에 삽입
						}
					}
				}
				
			}
//			for(int i=0; i<n; i++) {
//				System.out.println(Arrays.toString(distance[i]));
//			}
//			System.out.println();
			sb.append("Problem "+tc+": "+distance[n-1][n-1]).append("\n");
			tc += 1;
		}
		
		System.out.println(sb);
		
		
	}//main

}//class

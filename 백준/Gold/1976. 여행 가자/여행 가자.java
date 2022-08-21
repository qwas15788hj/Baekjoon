import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m;
	static int[][] graph; //연결 정보
	static boolean[][] CanGo; //갈 수 있는지
	static boolean[][] visited; //방문 처리
	static int[] route; //여행 경로
	static int idx;
	static boolean flag;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		graph = new int[n][n];
		CanGo = new boolean[n][n];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<n; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if(i==j) {
					CanGo[i][j] = true; //같은 위치면 갈 수 있음
				}
			}
		}
		
		route = new int[m];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<m; i++) {
			route[i] = Integer.parseInt(st.nextToken())-1;
		} //입력 완료
		
		for(int i=0; i<n; i++) {
			idx = i; //출발 지점
			visited = new boolean[n][n];
			dfs(i);
		}
		
		flag = true;
		for(int i=0; i<m-1; i++) {
			if(!(CanGo[route[i]][route[i+1]])) {
				flag = false;
				break;
			}
		}
		
		if(flag) System.out.println("YES");
		else System.out.println("NO");
		

	}//main
	
	public static void dfs(int start) {
		for(int i=0; i<n; i++) {
			if(graph[start][i]==1 && !(visited[start][i])) { //경유지 출발 지점~도착 지점까지 갈 수 있고, 방문 안했다면
				visited[start][i] = true; //방문 처리
				CanGo[idx][i] = true; //처음 시작 지점~도착 지점까지 갈 수 있음
				dfs(i);
			}
		}
	}

}//class

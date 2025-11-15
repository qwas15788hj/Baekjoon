import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		
		int[][] arr = new int[n][n];
		int INF = 1000000000;
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(i==j) continue;
				arr[i][j] = INF;
			}
		}
		for(int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken())-1;
			int b = Integer.parseInt(st.nextToken())-1;
			int price = Integer.parseInt(st.nextToken());
			if(arr[a][b] > price) {
				arr[a][b] = price;
			}
		}
		
		//플로이드 워샬 (경출도)
		for(int k=0; k<n; k++) {
			for(int i=0; i<n; i++) {
				if(i==k) continue;
				for(int j=0; j<n; j++) {
					if(k==j || i==j) continue;
					arr[i][j] = Math.min(arr[i][j], arr[i][k]+arr[k][j]);
				}
			}
		}
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(arr[i][j]==INF) {
					arr[i][j] = 0;
				}
			}
		}
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				sb.append(arr[i][j]+" ");
			}
			sb.append("\n");
		}
		
		System.out.println(sb);
		
	}

}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<t+1; tc++) {
			int n = Integer.parseInt(br.readLine());
			int[][] arr = new int[n][n];
			int num = 2;
			int[] dx = {0, 1, 0, -1};
			int[] dy = {1, 0, -1, 0};
			int x = 0;
			int y = 0;
			arr[x][y] = 1;
			
			int nx = 0;
			int ny = 0;
			while(true) {
				for(int i=0; i<4; i++) {
					while(true) {
						x += dx[i];
						y += dy[i];
						if(x>=0 && x<n && y>=0 && y<n && arr[x][y]==0) {
							arr[x][y] = num;
							num += 1;
						} else {
							x -= dx[i];
							y -= dy[i];
							break;
						}
					}
				}
				if(num==n*n+1) break;
			}//while
			
			System.out.println("#"+tc);
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					if(j==n-1) System.out.print(arr[i][j]);
					else System.out.print(arr[i][j]+" ");
				}
				System.out.println();
			}
			
			
		}//for (test_case)

	}

}

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	
	static int n, m, k, count;
	static int[][] arr;
	static int[][] command;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static int answer;
	static boolean[] select;
	static ArrayList<int[]> list;
	static int[] store;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		k = sc.nextInt();
		arr = new int[n][m];
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		
		answer = Integer.MAX_VALUE;
		command = new int[k][3];
		for(int i=0; i<k; i++) {
			for(int j=0; j<3; j++) {
				command[i][j] = sc.nextInt();
			}
		}//입력 종료
		
		select = new boolean[k];
		store = new int[k];
		count = 0;
		perm(0);
		
		
//		for(int i=0; i<k; i++) {
//			arr = turn(arr, command[i][0]-1, command[i][1]-1, command[i][2]);
////			System.out.println(Arrays.deepToString(arr));
//			sum();
//		}
		System.out.println(answer);
		
		

	}//main
	
	//줄때 r-1, c-1
	public static int[][] turn(int[][] arr, int r, int c, int s) {
		int[][] tArr = new int[n][m];
		int Xstart = r-s;
		int Ystart = c-s;
		int Xend = r+s;
		int Yend = c+s;
		int turn = (2*s+1)/2;
		for(int i=0; i<turn; i++) {
			int x = Xstart+i;
			int y = Ystart+i;
			for(int j=0; j<4; j++) {
				while(true) {
					int nx = x+dx[j];
					int ny = y+dy[j];
					if(nx>=Xstart+i && nx<=Xend-i && ny>=Ystart+i && ny<=Yend-i) {
						tArr[nx][ny] = arr[x][y];
						x = nx;
						y = ny;
					} else {
						break;
					}
				}
			}
		}
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(tArr[i][j]==0) {
					tArr[i][j] = arr[i][j];
				}
			}
		}
		return tArr;
		
	}//turn
	
	
	public static void sum(int[][] sarr) {
		for(int i=0; i<n; i++) {
			int count = 0;
			for(int j=0; j<m; j++) {
				count += sarr[i][j];
			}
			answer = Math.min(answer, count);
		}
	}//sum
	
	
	public static void perm(int count) {
		if(count==k) {
			int[][] sarr = arr;
			for(int i=0; i<k; i++) {
				sarr = turn(sarr, command[store[i]][0]-1, command[store[i]][1]-1, command[store[i]][2]);
//				System.out.println(Arrays.deepToString(sarr));
			}
			sum(sarr);
		}
		
		for(int i=0; i<k; i++) {
			if(select[i]) continue;
			
			store[count] = i;
			select[i] = true;
			perm(count+1);
			select[i] = false;
		}
		
	}//perm
	
	

}//class

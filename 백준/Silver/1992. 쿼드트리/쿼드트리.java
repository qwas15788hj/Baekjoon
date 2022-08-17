import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int[][] arr;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		arr = new int[n][n];
		for(int i=0; i<n; i++) {
			String str = br.readLine();
			for(int j=0; j<n; j++) {
				arr[i][j] = str.charAt(j)-'0';
			}
		}//입력 완료
		
		QuadTree(0, 0, n);
		System.out.println(sb);
	}//main
	
	public static void QuadTree(int x, int y, int size) {
		//압축 가능한 경우
		boolean flag = true;
		int start = arr[x][y];
		a:
		for(int i=x; i<x+size; i++) {
			for(int j=y; j<y+size; j++) {
				if(arr[i][j] != start) {
					flag = false;
					break a;
				}
			}
		}
		if(flag) {
			sb.append(start);
			return;
		}//압축 끝
		
		//압축 불가능
		sb.append("(");
		QuadTree(x, y, size/2); //왼쪽 위
		QuadTree(x, y+size/2, size/2); //오른쪽 위
		QuadTree(x+size/2, y, size/2); //왼쪽 아래
		QuadTree(x+size/2, y+size/2, size/2); //오른쪽 아래
		sb.append(")");
		
		
	}//QuadTree

}//class

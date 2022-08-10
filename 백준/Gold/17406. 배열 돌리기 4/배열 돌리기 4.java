import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	
	static int n, m, k, count;
	static int[][] arr; //배열 저장
	static int[][] command; //연산 저장
	static int[] dx = {0, 1, 0, -1}; //우, 하, 좌, 상
	static int[] dy = {1, 0, -1, 0};
	static int answer; //답
	static boolean[] select; //뽑았는지 확인 - 순열
	static int[] store; //연산 순서 저장할 배열(인덱스 값으로) - 순열
	
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
		
		System.out.println(answer);

	}//main
	
	//배열 돌려주는 메서드
	public static int[][] turn(int[][] arr, int r, int c, int s) {
		int[][] tArr = new int[n][m];
		int Xstart = r-s; //시작 값(세로 인덱스)
		int Ystart = c-s; //시작 값(가로 인덱스)
		int Xend = r+s; //마지막 값(세로 인덱스)
		int Yend = c+s; //마지막 값(가로 인덱스)
		int turn = (2*s+1)/2; //돌릴 테두리 개수
		for(int i=0; i<turn; i++) { //돌릴 테두리 개수 만큼
			int x = Xstart+i; //시작(세로 인덱스)
			int y = Ystart+i; //시작(가로 인덱스)
			for(int j=0; j<4; j++) { //4방향 (우, 하, 좌, 상)
				while(true) {
					int nx = x+dx[j]; //다음 방향
					int ny = y+dy[j]; //다음 방향
					if(nx>=Xstart+i && nx<=Xend-i && ny>=Ystart+i && ny<=Yend-i) { //범위 내에서만
						tArr[nx][ny] = arr[x][y];
						x = nx; //칸 이동
						y = ny; //칸 이동
					} else {
						break;
					}
				}
			}
		}
		//연산에 포함되지 않은 배열은 0이 들어있으므로 원래 배열(arr)에서 그대로 가져옴
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(tArr[i][j]==0) {
					tArr[i][j] = arr[i][j];
				}
			}
		}
		return tArr;
		
	}//turn
	
	//배열 각 행 합 구하기
	public static void sum(int[][] sarr) {
		for(int i=0; i<n; i++) {
			int count = 0;
			for(int j=0; j<m; j++) {
				count += sarr[i][j];
			}
			answer = Math.min(answer, count);
		}
	}//sum
	
	//연산 순서 구하기(순열)
	public static void perm(int count) {
		if(count==k) { //기저조건
			int[][] sarr = arr; //새로운 배열에 arr복사
			for(int i=0; i<k; i++) { //순열로 나오는 연산의 경우의 수 돌리기 i=store의 인덱스 값으로 접근
				sarr = turn(sarr, command[store[i]][0]-1, command[store[i]][1]-1, command[store[i]][2]);
			}
			sum(sarr); //최종 값 도출
		}
		
		//순열 구하기
		for(int i=0; i<k; i++) {
			if(select[i]) continue;
			
			store[count] = i;
			select[i] = true;
			perm(count+1);
			select[i] = false;
		}
		
	}//perm
	
	
}//class

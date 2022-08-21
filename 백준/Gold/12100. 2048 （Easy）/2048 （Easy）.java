import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int n, count, answer;
	static int[][] arr;
	static int[] move_numbers;
	static int[] dx = {0, 0, -1, 1}; //상하좌우, 가로값
	static int[] dy = {-1, 1, 0, 0}; //세로값
	static boolean[][] visited; //합친 블록
	static int total;
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		StringTokenizer st;
		arr = new int[n][n];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}//입력 완료
		
		move_numbers = new int[5];
		answer = 0;
//		total = 0;
		perm_repeat(0);
//		System.out.println(total);
		System.out.println(answer);

	}//main
	
	public static void perm_repeat(int count) { //4방향, 5번 이동, 중복 순열
		if(count==5) {
			total+=1;
			move(move_numbers);
			return;
		}
		
		for(int i=0; i<4; i++) {
			move_numbers[count] = i;
			perm_repeat(count+1);
		}
		
	}//perm_repeat
	
	public static void move(int[] move_numbers) {
		int[][] SubArr = new int[n][n];
		for(int i=0; i<arr.length; i++) {
			System.arraycopy(arr[i], 0, SubArr[i], 0, arr[i].length);
		}
		
		for(int k=0; k<move_numbers.length; k++) {
			visited = new boolean[n][n];
			int cnt = 0;
			switch (move_numbers[k]) {
			case 0:
				for(int i=0; i<n; i++) { //가로
					for(int j=0; j<n; j++) { //세로
						if(SubArr[j][i] != 0) {
							int nx = i; //가로
							int ny = j; //세로
//							int flag = 0;
							while(true) {
//								flag +=1;
								ny -= 1; //위로 올라가기
								if(nx>=0 && nx<n && ny>=0 && ny<n && SubArr[ny][nx]==0) {
									SubArr[ny][nx] = SubArr[ny+1][nx];
									SubArr[ny+1][nx] = 0;
								} else if(nx>=0 && nx<n && ny>=0 && ny<n && SubArr[ny][nx]==SubArr[ny+1][nx]) {
									if(!(visited[ny][nx])) {
										SubArr[ny][nx]*=2;
										visited[ny][nx] = true;
										SubArr[ny+1][nx] = 0;
										break;
									} else {
										break;
									}
								} else if(nx>=0 && nx<n && ny>=0 && ny<n && SubArr[ny][nx]!=SubArr[ny+1][nx]) {
									break;
								} else if(nx<0 || nx>=n || ny<0 || ny>=n) {
									break;
								}
								
							}//while
						}
					}
				}
				cnt = block(SubArr);
				answer = Math.max(answer, cnt);

				break;
				
			case 1:
				for(int i=0; i<n; i++) { //가로
					for(int j=n-1; j>=0; j--) { //세로
						if(SubArr[j][i] != 0) {
							int nx = i; //가로
							int ny = j; //세로
							while(true) {
								ny += 1; //아래로 내려가기
								if(nx>=0 && nx<n && ny>=0 && ny<n && SubArr[ny][nx]==0) {
									SubArr[ny][nx] = SubArr[ny-1][nx];
									SubArr[ny-1][nx] = 0;
								} else if(nx>=0 && nx<n && ny>=0 && ny<n && SubArr[ny][nx]==SubArr[ny-1][nx]) {
									if(!(visited[ny][nx])) {
										SubArr[ny][nx]*=2;
										visited[ny][nx] = true;
										SubArr[ny-1][nx] = 0;
										break;
									} else {
										break;
									}
								} else if(nx>=0 && nx<n && ny>=0 && ny<n && SubArr[ny][nx]!=SubArr[ny-1][nx]) {
									break;
								} else if(nx<0 || nx>=n || ny<0 || ny>=n) {
									break;
								}
								
							}//while
						}
					}
				}

				cnt = block(SubArr);
				answer = Math.max(answer, cnt);
				
				break;
			case 2:
				for(int j=0; j<n; j++) { //가로
					for(int i=0; i<n; i++) { //세로
						if(SubArr[j][i] != 0) {
							int nx = i; //가로
							int ny = j; //세로
							while(true) {
								nx -= 1; //왼쪽으로 가기
								if(nx>=0 && nx<n && ny>=0 && ny<n && SubArr[ny][nx]==0) {
									SubArr[ny][nx] = SubArr[ny][nx+1];
									SubArr[ny][nx+1] = 0;
								} else if(nx>=0 && nx<n && ny>=0 && ny<n && SubArr[ny][nx]==SubArr[ny][nx+1]) {
									if(!(visited[ny][nx])) {
										SubArr[ny][nx]*=2;
										visited[ny][nx] = true;
										SubArr[ny][nx+1] = 0;
										break;
									} else {
										break;
									}
								} else if(nx>=0 && nx<n && ny>=0 && ny<n && SubArr[ny][nx]!=SubArr[ny][nx+1]) {
									break;
								} else if(nx<0 || nx>=n || ny<0 || ny>=n) {
									break;
								}
								
							}//while
						}
					}
				}
				
				cnt = block(SubArr);
				answer = Math.max(answer, cnt);

				break;
			case 3:
				for(int j=0; j<n; j++) { //가로
					for(int i=n-1; i>=0; i--) { //세로
						if(SubArr[j][i] != 0) {
							int nx = i; //가로
							int ny = j; //세로
							while(true) {
								nx += 1; //오른쪽으로 가기
								if(nx>=0 && nx<n && ny>=0 && ny<n && SubArr[ny][nx]==0) {
									SubArr[ny][nx] = SubArr[ny][nx-1];
									SubArr[ny][nx-1] = 0;
								} else if(nx>=0 && nx<n && ny>=0 && ny<n && SubArr[ny][nx]==SubArr[ny][nx-1]) {
									if(!(visited[ny][nx])) {
										SubArr[ny][nx]*=2;
										visited[ny][nx] = true;
										SubArr[ny][nx-1] = 0;
										break;
									} else {
										break;
									}
								} else if(nx>=0 && nx<n && ny>=0 && ny<n && SubArr[ny][nx]!=SubArr[ny][nx-1]) {
									break;
								} else if(nx<0 || nx>=n || ny<0 || ny>=n) {
									break;
								}
								
							}//while
						}
					}
				}
				
				cnt = block(SubArr);
				answer = Math.max(answer, cnt);		

				break;
				
			default:
				
				break;
			}
			
		}
		
	}//move
	
	public static int block(int[][] SubArr) {
		int num = 0;
		for(int i=0; i<SubArr.length; i++) {
			for(int j=0; j<SubArr[0].length; j++) {
				if(SubArr[i][j] > num) {
					num = SubArr[i][j];
				}
			}
		}
		return num;
	}
	
}//class

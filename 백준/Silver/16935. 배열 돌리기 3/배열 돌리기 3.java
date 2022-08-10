import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m, r;
	static int[][] arr;
	static int[][] changeArr;
//	static ArrayList<Integer> type = new ArrayList<>();
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		st = new StringTokenizer(br.readLine());
		int[] type = new int[r];
		for(int i=0; i<r; i++) {
			type[i] = Integer.parseInt(st.nextToken());
		}
//		System.out.println(Arrays.toString(type));
		for(int i=0; i<r; i++) {
			switch(type[i]) {
			case 1:
				type1();
				break;
			case 2:
				type2();
				break;
			case 3:
				type3();
				break;
			case 4:
				type4();
				break;
			case 5:
				type5();
				break;
			case 6:
				type6();
				break;
				
			}//switch
			
		}//for
		for(int i=0; i<arr.length; i++) {
			for(int j=0; j<arr[i].length; j++) {
				sb.append(arr[i][j]+" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);

	}//main

	public static void type1() {
		int[][] changeArr = new int[n][m];
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				changeArr[n-i-1][j] = arr[i][j];
			}
		}
		
		arr = changeArr;
		
	}//type1
	
	public static void type2() {
		changeArr = new int[n][m];
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				changeArr[i][m-j-1] = arr[i][j];
			}
		}
		arr = changeArr;
		
	}//type2
	
	public static void type3() {
		changeArr = new int[m][n];
		
		int col = n-1;
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				changeArr[j][col] = arr[i][j];
			}
			col--;
		}
		int temp = n;
		n = m;
		m = temp;
		arr = changeArr;
		
	}//type3
	
	public static void type4() {
		changeArr = new int[m][n];
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				changeArr[m-1-j][i] = arr[i][j];
			}
		}
		int temp = n;
		n = m;
		m = temp;
		arr = changeArr;
	}//type4
	
	public static void type5() {
		changeArr = new int[n][m];
		int Xhalf = n/2;
		int Yhalf = m/2;
		for(int i=0; i<Xhalf; i++) {
			for(int j=0; j<Yhalf; j++) {
				changeArr[i][Yhalf+j] = arr[i][j];
			}
		}
		for(int i=0; i<Xhalf; i++) {
			for(int j=Yhalf; j<m; j++) {
				changeArr[Xhalf+i][j] = arr[i][j];
			}
		}
		for(int i=Xhalf; i<n; i++) {
			int col = 0;
			for(int j=Yhalf; j<m; j++, col++) {
				changeArr[i][col] = arr[i][j];
			}
		}
		
		int row = 0;
		for(int i=Xhalf; i<n; i++, row++) {
			for(int j=0; j<Yhalf; j++) {
				changeArr[row][j] = arr[i][j];
			}
		}
		arr = changeArr;
		
	}//type5
	
	public static void type6() {
		changeArr = new int[n][m];
		int Xhalf = n/2;
		int Yhalf = m/2;
		for(int i=0; i<Xhalf; i++) {
			for(int j=0; j<Yhalf; j++) {
				changeArr[i+Xhalf][j] = arr[i][j];
			}
		}
		for(int i=Xhalf; i<n; i++) {
			for(int j=0; j<Yhalf; j++) {
				changeArr[i][Yhalf+j] = arr[i][j];
			}
		}
		int row = 0;
		for(int i=Xhalf; i<n; i++, row++) {
			for(int j=Yhalf; j<m; j++) {
				changeArr[row][j] = arr[i][j];
			}
		}
		for(int i=0; i<Xhalf; i++) {
			int col = 0;
			for(int j=Yhalf; j<m; j++, col++) {
				changeArr[i][col] = arr[i][j];
			}
		}
		arr = changeArr;
		
	}
	
}//class

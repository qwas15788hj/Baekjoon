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
//	static int Xhalf, Yhalf; // 세로반, 가로반, 3, 4
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
		
//		while(st.hasMoreTokens()) {
//			type.add(Integer.parseInt(st.nextToken()));
//		} //입력 완료
//		type1();
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
		changeArr = new int[n][m];
		int line = n-1;
		int Xhalf = n/2;
		int Yhalf = m/2;
		for(int i=0; i<Xhalf; i++) {
			for(int j=0; j<m; j++) {
				changeArr[i+line][j] = arr[i][j];
			}
			line-=2;
		}
		
		line = -1;
		for(int i=Xhalf; i<n; i++) {
			for(int j=0; j<m; j++) {
				changeArr[i+line][j] = arr[i][j];
			}
			line-=2;
		}
		arr = changeArr;
		
	}//type1
	
	public static void type2() {
		changeArr = new int[n][m];
		int Xhalf = n/2;
		int Yhalf = m/2;
		int line = m-1;
		for(int i=0; i<Yhalf; i++) {
			for(int j=0; j<n; j++) {
				changeArr[j][i+line] = arr[j][i];
			}
			line-=2;
		}
		
		line = -1;
		for(int i=Yhalf; i<m; i++) {
			for(int j=0; j<n; j++) {
				changeArr[j][i+line] = arr[j][i];
			}
			line-=2;
		}
		arr = changeArr;
		
	}//type2
	
	public static void type3() {
		changeArr = new int[m][n];
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				changeArr[j][n-1-i] = arr[i][j];
			}
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
				changeArr[i][j] = arr[i+Xhalf][j];
			}
		}
		for(int i=0; i<Xhalf; i++) {
			for(int j=Yhalf; j<m; j++) {
				changeArr[i][j] = arr[i][j-Yhalf];
			}
		}
		for(int i=Xhalf; i<n; i++) {
			for(int j=0; j<Yhalf; j++) {
				changeArr[i][j] = arr[i][j+Yhalf];
			}
		}
		for(int i=Xhalf; i<n; i++) {
			for(int j=Yhalf; j<m; j++) {
				changeArr[i][j] = arr[i-Xhalf][j];
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
				changeArr[i][j] = arr[i][j+Yhalf];
			}
		}
		for(int i=0; i<Xhalf; i++) {
			for(int j=Yhalf; j<m; j++) {
				changeArr[i][j] = arr[i+Xhalf][j];
			}
		}
		for(int i=Xhalf; i<n; i++) {
			for(int j=0; j<Yhalf; j++) {
				changeArr[i][j] = arr[i-Xhalf][j];
			}
		}
		for(int i=Xhalf; i<n; i++) {
			for(int j=Yhalf; j<m; j++) {
				changeArr[i][j] = arr[i][j-Yhalf];
			}
		}
		arr = changeArr;
		
	}
	
}//class

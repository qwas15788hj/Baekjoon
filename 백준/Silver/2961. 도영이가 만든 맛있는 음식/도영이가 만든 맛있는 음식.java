import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int n;
	static int[] sourArr;
	static int[] bitterArr;
	static boolean[] select;
	static int answer;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		sourArr = new int[n];
		bitterArr = new int[n];
		select = new boolean[n];
		for(int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			sourArr[i] = Integer.parseInt(st.nextToken());
			bitterArr[i] = Integer.parseInt(st.nextToken());
		}

		answer = Integer.MAX_VALUE;
		subset(0);
		System.out.println(answer);

	}//main

	
	public static void subset(int index) {
		if(index==n) {
			boolean flag = false;
			for(int i=0; i<n; i++) {
				if(select[i]) {
					flag = true;
					break;
				}
			}
			if(flag) {
				int sour = 1;
				int bitter = 0;
				for(int i=0; i<n; i++) {
					if(select[i]) {
						sour *= sourArr[i];
						bitter += bitterArr[i];
					}
				}
//				System.out.println(Math.abs(sour-bitter));
				answer = Math.min(answer, Math.abs(sour-bitter));
			}
			return;
		}
		
		select[index] = true;
		subset(index+1);
		select[index] = false;
		subset(index+1);
		
	}//subset
	
	
}//class

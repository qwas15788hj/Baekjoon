import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Solution {
	
	static int count; //뽑은 수(조건)
	static int[] Kyuarr = new int[9]; //규영 배열
	static int[] Inarr = new int[9]; //인영 배열
	static boolean[] select = new boolean[9]; //골랐는지(순열)
	static int[] store = new int[9]; //고른 수 저장(순열)
	static int win; //이긴 수
	static int lose; //진 수
	
	public static void main(String[] args) throws IOException {
		
//		BufferedReader br = new BufferedReader(new FileReader("6808_input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<t+1; tc++) {
			boolean[] flag = new boolean[19]; //인영이 카드를 얻기 위한 배열
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int i=0; i<9; i++) {
				int num = Integer.parseInt(st.nextToken());
				Kyuarr[i] = num;
				flag[num] = true; //규영이 뽑은 수 표시
			}
			
			int idx = 0;
			//인영이 뽑을 수
			for(int i=1; i<flag.length; i++) {
				if(!(flag[i])) {
					Inarr[idx] = i;
					idx += 1;
				}
			}
			
			win = 0;
			lose = 0;
			perm(0);
			
			System.out.println("#"+tc+" "+win+" "+lose);
		}//for(test_case)

	}//main
	
	private static void perm(int count) { //인영이 뽑을 수 있는 수 종류(순열)
		if(count==9) { //9개 뽑으면 stop
			game(store);
		}//if
		
		
		for(int i=0; i<9; i++) {
			if(select[i]) continue; //뽑았으면 무시
			//안뽑은 수
			store[count] = Inarr[i]; //저장
			select[i] = true; //뽑은 표시
			perm(count+1);
			select[i] = false;
			
		}//for
		
	}//perm
	
	
	private static void game(int[] perm_Inarr) {
		int KyuScore = 0; //규영 점수
		int InScore = 0; //인영 점수
		for(int i=0; i<9; i++) {
			if(Kyuarr[i] > perm_Inarr[i]) { //규연이 뽑은 수 > 인영이 뽑은 수
				KyuScore += Kyuarr[i]+perm_Inarr[i];
			} else {
				InScore += Kyuarr[i]+perm_Inarr[i];
			}
		}
		
		if(KyuScore > InScore) {
			win+=1;
		}
		else if(InScore > KyuScore) {
			lose+=1;
		}
		
	}//game
	

}//class

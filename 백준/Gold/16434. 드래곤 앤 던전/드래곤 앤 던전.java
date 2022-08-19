import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()); //방 개수
		long Hatk = Long.parseLong(st.nextToken()); //용사 공격력
		long Hmaxhp = 0; //용사 최대 체력
		long Hcurhp = 0; //용사 현재 체력
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			int t = Integer.parseInt(st.nextToken()); //1번 or 2번
			int a = Integer.parseInt(st.nextToken()); //공격력
			long h = Long.parseLong(st.nextToken()); //생명력
			
			if(t==1) {
				int div = 0;
				if(h%Hatk==0) { //나누어지면 마지막 때릴때 안맞으니 -1
					div = 1;
				}
				Hcurhp += a*(h/Hatk - div); //몬스터 공격력*(체력/용사공격력 - 막타 여부)
				Hmaxhp = Math.max(Hmaxhp, Hcurhp); //최대체력 저장
//				System.out.println(Hcurhp);
//				System.out.println(Hmaxhp);
				
			} else {
				Hatk += a; //공격력 증가
				Hcurhp = Math.max(Hcurhp-h, 0); //현재 체력-물략, 물략이 크면 0
				
				
//				if(h > Math.abs(Hcurhp)) {
//					Hcurhp = 0;
//				} else {
//					Hcurhp += h;
//				}
			}
			
		}//for(방 개수)
		
		System.out.println(Hmaxhp+1);
		
		
	}//main

}//class

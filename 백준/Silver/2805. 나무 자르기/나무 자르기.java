import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int[] arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		long start = 1;
		long end = arr[n-1];
		long answer = 0;
		while(start <= end) {
			long total = 0; //자른 길이
			long mid = (start+end)/2;
			for(int i=0; i<n; i++) { //나무 마다
				if(arr[i] > mid) { //절단 길이 크면
					total += arr[i]-mid; //나무 길이-절단 길이
				}
			}//for
			
			if(total < m) { //절단기가 너무 김
				end = mid-1;
			} else { //절단기가 짧아서 m길이 이상 나옴
				answer = mid; //일단 저장
				start = mid+1; //절단기 길이 늘리기
			}
			
		}//while
		
		System.out.println(answer);
		
	}//main

}//class

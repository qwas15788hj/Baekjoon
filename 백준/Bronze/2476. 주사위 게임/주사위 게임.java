import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		
		for(int i=0; i<n; i++) {
			int money = 0;
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			
			if(a==b && a==c && b==c) {
				money = 10000+a*1000;
			} else if(a==b || a==c) {
				money = 1000+a*100;
			} else if(b==c) {
				money = 1000+b*100;
			} else {
				money = Math.max(a, Math.max(b, c))*100;
			}
			arr[i] = money;
		}
		Arrays.sort(arr);
		System.out.println(arr[n-1]);
	}

}

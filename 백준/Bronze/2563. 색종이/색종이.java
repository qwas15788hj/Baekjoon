import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		boolean[][] arr = new boolean[101][101];
		int count = 0;
		for(int i=0; i<n; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			for(int a=x; a<x+10; a++) {
				for(int b=y; b<y+10; b++) {
					if(!(arr[a][b])) {
						arr[a][b] = true;
						count+=1;
					}
				}
			}
		}
		System.out.println(count);

	}//main

}//class

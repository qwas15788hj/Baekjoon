import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		boolean[][] visited = new boolean[1001][1001];
		ArrayList<int[]> arr = new ArrayList<>();
		int n = sc.nextInt();
		for(int k=0; k<n; k++) {
			int[] arr2 = new int[4];
			for(int i=0; i<4; i++) {
				arr2[i] = sc.nextInt();
			}
			arr.add(arr2);
		}
		
		int[] out = new int[n];
		for(int k=arr.size()-1; k>=0; k--) {
			int count = 0;
			for(int i=arr.get(k)[0]; i<arr.get(k)[0]+arr.get(k)[2]; i++) {
				for(int j=arr.get(k)[1]; j<arr.get(k)[1]+arr.get(k)[3]; j++) {
					if(!(visited[i][j])) {
						count += 1;
						visited[i][j] = true;
					}
				}
			}
			out[k] = count;
		}
		
		for(int i=0; i<out.length; i++) {
			System.out.println(out[i]);
		}
		
	}//main

}//class

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m, count=0;
	static int[] store;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		store = new int[m];
		
		overperm(0);
		System.out.println(sb);
		
	}//main
	
	private static void overperm(int count) {
		if(count==m) {
			for(int i=0; i<store.length; i++) {
				sb.append(store[i]+" ");
			}
			sb.append("\n");
			return;
		}
		
		for(int i=1; i<=n; i++) {
			store[count] = i;
			overperm(count+1);
		}
		
	}//overperm
	
}//class
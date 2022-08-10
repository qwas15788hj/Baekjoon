import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	
	static int n, k;
	static int[] visited;
	static boolean[] select;
	static int time, count;
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		k = sc.nextInt();
		
		visited = new int[100001];
		select = new boolean[100001];
		time = 0;
		count = 0;
		bfs(n);
		System.out.println(time);
		System.out.println(count);
		
	}//main
	
	private static void bfs(int start) {
		if(n==k) {
			time = 0;
			count = 1;
			return;
		}
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(start);
		int ms = 0;
		while(time==0) {
			int qsize = queue.size();
			for(int i=0; i<qsize; i++) {
				int temp = queue.poll();
				select[temp] = true;
				if(ms==0) select[temp] = false;
				if(temp==k) {
					time = ms;
					count += 1;
				}
				if(temp-1>=0 && temp-1<100001 && !(select[temp-1])) {
					queue.offer(temp-1);
				}
				if(temp+1>=0 && temp+1<100001 && !(select[temp+1])) {
					queue.offer(temp+1);
				}
				if(temp*2>=0 && temp*2<100001 && !(select[temp*2])) {
					queue.offer(temp*2);
				}
			}
			
			ms += 1;
//			System.out.println(queue);
			
		}//while(time)
				
	}//bfs

}//class

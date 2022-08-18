import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class Main {
	
	static int n, k;
	static int[] visited;
	static boolean[] select;
	static int time, count;
	static int[] check;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		n = sc.nextInt();
		k = sc.nextInt();
		
		visited = new int[100001];
		select = new boolean[100001];
		check = new int[100001];
		time = 0;
		count = 0;
		
//		System.out.println(count);
//		System.out.println(Arrays.toString(check));
		if(n==k) {
			sb.append(0+"\n");
			sb.append(n);
		} else {
			bfs(n);
			sb.append(time).append("\n");
			
			Stack<Integer> stack = new Stack<>();
			stack.add(k);
			int idx = k;
			while(idx!=n) {
				stack.push(check[idx]);
				idx = check[idx];
			}
			
			while(!stack.isEmpty()) {
				sb.append(stack.pop()).append(" ");
			}
			
		}
		System.out.println(sb);
		
	}//main
	
	public static void bfs(int start) {
		time = 0;
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(start);
		select[start] = true;
		
		while(!queue.isEmpty()) {
			if(select[k]) {
				return;
			}
			int qsize = queue.size();
			for(int i=0; i<qsize; i++) {
				int temp = queue.poll();
//				select[temp] = true;
				
				if(temp-1>=0 && temp-1<100001 && !(select[temp-1])) {
					select[temp-1] = true;
					check[temp-1] = temp;
					queue.offer(temp-1);
				}
				if(temp+1>=0 && temp+1<100001 && !(select[temp+1])) {
					select[temp+1] = true;
					check[temp+1] = temp;
					queue.offer(temp+1);
				}
				if(temp*2>=0 && temp*2<100001 && !(select[temp*2])) {
					select[temp*2] = true;
					check[temp*2] = temp;
					queue.offer(temp*2);
				}
			}
			
			time += 1;
//			System.out.println(queue);
		}//while(time)
				
	}//bfs
	
	
}//class

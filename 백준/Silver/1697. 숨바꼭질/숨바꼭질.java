import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int n, k;
	static int[] arr;
	static boolean[] visited;
	static int time;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		arr = new int[100001];
		visited = new boolean[100001];
		
		time = 0;
		if(n==k) {
			System.out.println(0);
		} else {
			bfs(n);
			System.out.println(time);
		}
		
	}//main
	
	public static void bfs(int start) {
		Queue<Integer> queue = new LinkedList<>();
		queue.offer(start);
		visited[start] = true;
		while(!(queue.isEmpty())) {
			int size = queue.size();
			for(int i=0; i<size; i++) {
				int temp = queue.poll();
				if(temp==k) {
					return;
				}
				
				if(temp-1>=0 && temp-1<100001 && !(visited[temp-1])) {
					queue.add(temp-1);
					visited[temp-1] = true;
				}
				if(temp+1>=0 && temp+1<100001 && !(visited[temp+1])) {
					queue.add(temp+1);
					visited[temp+1] = true;
				}
				if(temp*2>=0 && temp*2<100001 && !(visited[temp*2])) {
					queue.add(temp*2);
					visited[temp*2] = true;
				}
				
			}
			time += 1;
			
		}//while
		
	}//bfs
	
}//class

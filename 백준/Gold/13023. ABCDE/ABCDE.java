import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m;
	static ArrayList<Integer>[] list;
	static boolean[] visited;
	static boolean flag;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		list = new ArrayList[n];
		for(int i=0; i<n; i++) {
			list[i] = new ArrayList<>();
		}
		visited = new boolean[n];
		for(int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			list[a].add(b);
			list[b].add(a);
		}
//		System.out.println(Arrays.toString(list));
		for(int i=0; i<n; i++) {
			if(!(visited[i])) {
				dfs(i, 1);
				visited[i] = false;
				if(flag) break;
			}
		}
		
		if(flag) System.out.println(1);
		else System.out.println(0);
		

	}//main
	
	public static void dfs(int start, int depth) {
		visited[start] = true;
		if(depth==5) {
			flag = true;
			return;
		}
		
		for(int i=0; i<list[start].size(); i++) {
			int temp = list[start].get(i);
			if(!(visited[temp])) {
				dfs(temp, depth+1);
				visited[temp] = false;
			}
		}
		
	}//dfs
	
	
}//class

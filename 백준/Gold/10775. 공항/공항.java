import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	
	static int g, p;
	static int[] parent;
	static int[] visited;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		g = Integer.parseInt(br.readLine());
		p = Integer.parseInt(br.readLine());
		
		make();
		int answer = 0;
		
		for(int i=0; i<p; i++) {
			int airport = Integer.parseInt(br.readLine());
			int gate = find(airport);
			if(gate==0) {
				break;
			}
//			System.out.println(gate);
			union(gate-1, gate);
			answer += 1;
//			System.out.println(Arrays.toString(parent));
		}
		System.out.println(answer);
		
	}//main
	
	public static void make() {
		parent = new int[g+1];
		for(int i=0; i<g+1; i++) {
			parent[i] = i;
		}
	}
	
	public static int find(int a) {
		if(parent[a]==a) return a;
		return parent[a] = find(parent[a]);
	}
	
	public static boolean union(int a, int b) {
		int aRoot = find(a);
		int bRoot = find(b);
//		System.out.println(aRoot+" "+bRoot);
		if(aRoot==bRoot) return false;
		
		parent[bRoot] = aRoot;
		return true;
	}

}//class

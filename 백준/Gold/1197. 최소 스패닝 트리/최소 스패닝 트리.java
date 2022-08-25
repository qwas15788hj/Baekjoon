import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static class Edge implements Comparable<Edge> {
		
		int start, end, cost;

		public Edge(int start, int to, int cost) {
			super();
			this.start = start;
			this.end = to;
			this.cost = cost;
		}

		@Override
		public int compareTo(Edge o) {
			return this.cost-o.cost;
		}
		
	}
	
	static int v, e;
	static Edge[] edgelist;
	static int[] parents;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		v = Integer.parseInt(st.nextToken());
		e = Integer.parseInt(st.nextToken());
		
		make();
		edgelist = new Edge[e];
		for(int i=0; i<e; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			edgelist[i] = new Edge(a, b, c);
		}
		Arrays.sort(edgelist);
		
		long answer = 0;
		int count = 0;
		for(Edge edge: edgelist) {
			if(union(edge.start, edge.end)) {
				answer += edge.cost;
				if(++count==v-1) break;
			}
			
		}
		
		System.out.println(answer);
		

	}//main
	
	public static void make() {
		parents = new int[v+1];
		for(int i=0; i<v+1; i++) {
			parents[i] = i;
		}
	}
	
	public static int find(int a) {
		if(parents[a]==a) return a;
		return parents[a] = find(parents[a]);
	}
	
	public static boolean union(int a, int b) {
		int aRoot = find(a);
		int bRoot = find(b);
		
		if(aRoot==bRoot) return false;
		
		parents[bRoot] = aRoot;
		return true;
		
	}

}//class

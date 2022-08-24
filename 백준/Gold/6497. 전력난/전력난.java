import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static class Edge implements Comparable<Edge> {
		
		int start, end, cost;
		
		public Edge(int start, int end, int cost) {
			super();
			this.start = start;
			this.end = end;
			this.cost = cost;
		}

		@Override
		public int compareTo(Edge o) {
			return this.cost-o.cost; //가격을 기준으로 오름차순
		}
		
	}//Edge class
	
	static int m, n; //집의 수, 길의 수
	static int[] parents; //대표자 저장
	static Edge[] edgelist;
	static int sum; //총 사용되는 비용
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		while(true) {
			st = new StringTokenizer(br.readLine());
			m = Integer.parseInt(st.nextToken());
			n = Integer.parseInt(st.nextToken());
			if(m==0 && n==0) break;
			make();
			edgelist = new Edge[n];
			sum = 0;
			for(int i=0; i<n; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				sum += c;
				edgelist[i] = new Edge(a, b, c);
			}//간선 정보 저장 완료
			
			Arrays.sort(edgelist);
			int price = 0;
			int count = 0;
			for(Edge edge: edgelist) {
				if(union(edge.start, edge.end)) {
					price += edge.cost;
					if(++count==m-1) break;
				}
			}
			
			System.out.println(sum-price);
		}

	}//main
	
	public static void make() {
		parents = new int[m];
		for(int i=0; i<m; i++) {
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

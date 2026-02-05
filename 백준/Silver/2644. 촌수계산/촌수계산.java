import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    static Integer n, s, e, x, a, b, q;
    static int[][] arr;
    static int[] visited;
    static Queue<Integer> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {

        n = Integer.parseInt(br.readLine());
        arr = new int[n+1][n+1];
        visited = new int[n+1];
        for(int i=0; i<n+1; i++) {
            visited[i] = -1;
        }
        st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(br.readLine());
        for(int i=0; i<x; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            arr[a][b] = 1;
            arr[b][a] = 1;
        }

        bfs();
        System.out.println(visited[e]);

    }

    public static void bfs() {
        queue.offer(s);
        visited[s] = 0;
        while(!queue.isEmpty()) {
            q = queue.poll();
            for(int k=0; k<n+1; k++) {
                if(arr[q][k] == 1 && visited[k] == -1) {
                    queue.offer(k);
                    visited[k] = visited[q] + 1;
                }
            }
        }
    }
}

import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    static Integer n, m, v, a, b, q;
    static int[][] arr;
    static Queue<Integer> queue;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());
        arr = new int[n+1][n+1];
        queue = new LinkedList<>();
        visited = new boolean[n+1];
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            arr[a][b] = arr[b][a] = 1;
        }

        dfs(v);
        sb.append("\n");
        queue = new LinkedList<>();
        visited = new boolean[n+1];
        bfs(v);

        System.out.println(sb);
    }

    public static void dfs(int start) {
        visited[start] = true;
        sb.append(start + " ");
        for(int i = 0; i < n+1; i++) {
            if(arr[start][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }

    public static void bfs(int start) {
        queue.add(start);
        visited[start] = true;
        while(!queue.isEmpty()) {
            q = queue.poll();
            sb.append(q + " ");
            for(int i = 0; i < n+1; i++) {
                if(arr[q][i] == 1 && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }

}

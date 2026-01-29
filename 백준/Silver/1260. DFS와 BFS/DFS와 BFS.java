import java.io.*;
import java.util.*;
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    static Integer n;
    static Integer m;
    static Integer v;
    static int[][] arr;
    static boolean[] visited;
    static Queue<Integer> queue = new LinkedList<>();
    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());
        arr = new int[n+1][n+1];
        visited = new boolean[n+1];

        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            Integer a = Integer.parseInt(st.nextToken());
            Integer b = Integer.parseInt(st.nextToken());
            arr[a][b] = arr[b][a] = 1;
        }

        dfs(v);
        sb.append("\n");
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
            Integer x = queue.poll();
            sb.append(x + " ");
            for(int i = 0; i < n+1; i++) {
                if(arr[x][i] == 1 && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }
}

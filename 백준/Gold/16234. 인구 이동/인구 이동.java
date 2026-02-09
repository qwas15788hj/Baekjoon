import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    static int n, l, r, num, answer;
    static int[][] arr;
    static Queue<int[]> queue;
    static int[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1 ,1};
    static HashMap<Integer, Integer> group;
    static HashMap<Integer, Integer> person;

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        arr = new int[n][n];
        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        answer = 0;
        while(true) {
            queue = new LinkedList<>();
            visited = new int[n][n];
            group = new HashMap<>();
            person = new HashMap<>();
            num = 1;
            for(int i=0; i<n; i++) {
                for(int j=0; j<n; j++) {
                    if(visited[i][j] == 0) {
                        check(i, j);
                        num += 1;
                    }
                }
            }

            if(num == n*n+1) break;
            move();
            answer += 1;
        }

        System.out.println(answer);

    }

    public static void check(int a, int b) {
        queue.offer(new int[] {a, b});
        visited[a][b] = num;
        group.put(num, 1);
        person.put(num, arr[a][b]);
        while(!queue.isEmpty()) {
            int[] now = queue.poll();
            int x = now[0];
            int y = now[1];
            for(int k=0; k<4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if(0 <= nx && nx < n && 0 <= ny && ny < n && visited[nx][ny] == 0
                        && l <= Math.abs(arr[x][y] - arr[nx][ny])
                        && Math.abs(arr[x][y] - arr[nx][ny]) <= r) {
                    queue.offer(new int[] {nx, ny});
                    visited[nx][ny] = num;
                    group.put(num, group.get(num) + 1);
                    person.put(num, person.get(num) + arr[nx][ny]);
                }
            }
        }
    }

    public static void move() {
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                int idx = visited[i][j];
                arr[i][j] = person.get(idx)/group.get(idx);
            }
        }
    }
}

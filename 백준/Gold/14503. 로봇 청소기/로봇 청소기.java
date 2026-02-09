import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    static int n, m, r, c, d, answer;
    static int[][] arr;
    static boolean[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static boolean flag = true;

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        visited = new boolean[n][m];
        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        answer = 0;
        while(flag) {
            // 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소
            if(arr[r][c] == 0 && !visited[r][c]) {
                visited[r][c] = true;
                answer += 1;
            }

            // 주변 4칸 청소되어 있는지 체크
            boolean check = true;
            for(int k=0; k<4; k++) {
                int nx = r + dx[k];
                int ny = c + dy[k];
                if(0 <= nx && nx < n && 0 <= ny && ny < m && arr[nx][ny] == 0 && !visited[nx][ny]) {
                    check = false;
                    break;
                }
            }

            // 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
            if(check) {
                int nd = (d+2)%4;
                int nx = r + dx[nd];
                int ny = c + dy[nd];
                // 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
                if(0 <= nx && nx < n && 0 <= ny && ny < m && arr[nx][ny] == 0) {
                    r = nx;
                    c = ny;
                } else { // 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
                    flag = false;
                    break;
                }
            } else { // 3 .현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
                d = (d+3)%4; // 3-1. 반시계 방향으로 90도 회전한다.
                int nx = r + dx[d];
                int ny = c + dy[d];
                // 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
                if(0 <= nx && nx < n && 0 <= ny && ny < m && arr[nx][ny] == 0 && !visited[nx][ny]) {
                    r = nx;
                    c = ny;
                }
            }

        }

        System.out.println(answer);
    }
}

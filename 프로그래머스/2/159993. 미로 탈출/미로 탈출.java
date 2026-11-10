import java.util.*;
import java.io.*;
class Solution {
    int n, m;
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};
    String[] map;
    int sx, sy, lx, ly, ex, ey;
    
    public int solution(String[] maps) {
        int answer = 0;
        n = maps.length;
        m = maps[0].length();
        map = maps;
        
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(maps[i].charAt(j) == 'S') {
                    sx = i;
                    sy = j;
                }
                if(maps[i].charAt(j) == 'L') {
                    lx = i;
                    ly = j;
                }
                if(maps[i].charAt(j) == 'E') {
                    ex = i;
                    ey = j;
                }
            }
        }
        
        int result1 = bfs(sx, sy, lx, ly);
        int result2 = bfs(lx, ly, ex, ey);
        
        if(result1 == -1 || result2 == -1) {
            return -1;
        } else {
            return result1 + result2;
        }
    }
    
    public int bfs(int a, int b, int tx, int ty) {
        Queue<int[]> queue = new LinkedList<>();
        int[][] visited = new int[n][m];
        queue.offer(new int[]{a, b});
        visited[a][b] = 1;
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];
            if(x == tx && y == ty) {
                return visited[x][y] - 1;
            }
            for(int k=0; k<4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if(0 <= nx && nx < n && 0 <= ny && ny < m && map[nx].charAt(ny) != 'X' && visited[nx][ny] == 0) {
                    queue.offer(new int[]{nx, ny});
                    visited[nx][ny] = visited[x][y] + 1;
                }
            }
        }
        
        return -1;
    }
}
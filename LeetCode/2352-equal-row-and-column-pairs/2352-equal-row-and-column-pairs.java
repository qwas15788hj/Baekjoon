import java.util.*;
import java.io.*;
class Solution {
    public int equalPairs(int[][] grid) {
        int n = grid.length;
        int answer = 0;
        for(int i=0; i<n; i++) {
            int[] col = new int[n];
            for(int j=0; j<n; j++) {
                col[j] = grid[j][i];
                for(int k=0; k<n; k++) {
                    if(Arrays.equals(grid[k], col)) {
                        answer += 1;
                    }
                }
            }
        }

        return answer;
    }
}
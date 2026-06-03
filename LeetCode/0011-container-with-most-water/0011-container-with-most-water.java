import java.io.*;
import java.util.*;
class Solution {
    public int maxArea(int[] height) {
        int s = 0;
        int e = height.length-1;
        int answer = 0;

        while(s != e) {
            int area = (e-s) * Math.min(height[s], height[e]);

            answer = Math.max(answer, area);
            if(height[s] > height[e]) {
                e -= 1;
            } else {
                s += 1;
            }
        }
        return answer;
    }
}
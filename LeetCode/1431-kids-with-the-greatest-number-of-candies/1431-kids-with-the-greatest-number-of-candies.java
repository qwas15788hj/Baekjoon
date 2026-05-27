import java.util.*;
import java.io.*;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int n = candies.length;
        List<Boolean> answer = new ArrayList<>();
        int max = 0;
        for(int i=0; i<n; i++) {
            max = Math.max(max, candies[i]);
        }

        for(int i=0; i<n; i++) {
            if(candies[i] + extraCandies >= max) {
                answer.add(true);
            } else {
                answer.add(false);
            }
        }

        return answer;
    }
}
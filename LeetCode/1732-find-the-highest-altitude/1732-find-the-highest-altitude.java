import java.io.*;
import java.util.*;
class Solution {
    public int largestAltitude(int[] gain) {
        int n = gain.length;
        int[] arr = new int[n+1];
        for(int i=0; i<n; i++) {
            arr[i+1] = arr[i] + gain[i];
        }
        
        int answer = -Integer.MAX_VALUE;
        for(int i=0; i<n+1; i++) {
            answer = Math.max(answer, arr[i]);
        }

        return answer;
    }
}
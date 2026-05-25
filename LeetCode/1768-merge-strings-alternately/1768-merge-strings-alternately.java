import java.util.*;
import java.io.*;

class Solution {
    public String mergeAlternately(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        int min = Math.min(n, m);
        String answer = "";

        for(int i=0; i<min; i++) {
            answer += word1.charAt(i);
            answer += word2.charAt(i);
        }
        
        if(n > m) {
            answer += word1.substring(m, n);
        } else {
            answer += word2.substring(n, m);
        }

        return answer;
    }
}
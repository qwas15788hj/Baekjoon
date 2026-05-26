import java.util.*;
import java.io.*;

class Solution {
    public String gcdOfStrings(String str1, String str2) {
        int n = str1.length();
        int m = str2.length();
        int min = Math.min(n, m);
        
        String answer = "";
        for(int i=1; i<min+1; i++) {
            if(n%i==0 && m%i==0) {
                String s = str1.substring(0, i);
                String s1 = "";
                String s2 = "";
                for(int j=0; j<n/i; j++) {
                    s1 += s;
                }
                for(int j=0; j<m/i; j++) {
                    s2 += s;
                }
                if(s1.equals(str1) && s2.equals(str2)) {
                    answer = s;
                }
            }
        }

        return answer;
    }
}
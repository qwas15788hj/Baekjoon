import java.io.*;
import java.util.*;
class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.equals("")) return true;
        
        int n = s.length();
        int m = t.length();
        int idx = 0;
        for(int i=0; i<m; i++) {
            if(s.charAt(idx) == t.charAt(i)) {
                idx += 1;
            }
            if(idx == n) {
                return true;
            }
        }
        return false;
    }
}
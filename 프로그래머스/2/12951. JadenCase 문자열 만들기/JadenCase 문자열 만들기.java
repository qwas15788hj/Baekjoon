import java.io.*;
import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        
        String lowStr = s.toLowerCase();
        boolean flag = true;
        for(int i=0; i<lowStr.length(); i++) {
            char c = lowStr.charAt(i);
            
            if(c == ' ') {
                answer += c;
                flag = true;
            } else {
                if(flag) {
                    answer += Character.toUpperCase(c);
                    flag = false;
                } else {
                    answer += c;
                }
            }
        }
        
        return answer;
    }
}
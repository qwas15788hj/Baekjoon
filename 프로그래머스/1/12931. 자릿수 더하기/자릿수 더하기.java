import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        String sn = Integer.toString(n);
        for(int i=0; i<sn.length(); i++) {
            answer += sn.charAt(i) - '0';
        }

        return answer;
    }
}
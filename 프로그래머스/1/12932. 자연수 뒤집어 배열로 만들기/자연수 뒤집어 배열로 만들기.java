import java.util.*;

class Solution {
    public int[] solution(long n) {
        String sn = Long.toString(n);
        
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = sn.length() - 1; i >= 0; i--) {
            arr.add(sn.charAt(i) - '0');
        }
        
        int[] answer = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            answer[i] = arr.get(i);
        }
        
        return answer;
    }
}
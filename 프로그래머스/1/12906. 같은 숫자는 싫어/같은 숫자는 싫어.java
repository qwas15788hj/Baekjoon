import java.util.*;
import java.io.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> result = new ArrayList<>();
        result.add(arr[0]);
        for(int i=1; i<arr.length; i++) {
            if(arr[i] != result.get(result.size()-1)) {
                result.add(arr[i]);
            }
        }
        
        int[] answer = new int[result.size()];
        for(int i=0; i<result.size(); i++) {
            answer[i] = result.get(i);
        }
        
        return answer;
        
    }
}
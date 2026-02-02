import java.io.*;
import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        int n = clothes.length;
        
        HashMap<String, Integer> map = new HashMap<>();
        for(int i=0; i<n; i++) {
            String type = clothes[i][1];
            if(map.containsKey(type)) {
                map.put(type, map.get(type)+1);
            } else {
                map.put(type, 1);
            }
        }
        
        for(Integer value : map.values()) {
            answer *= (value + 1);
        }
        
        return answer - 1;
    }
}
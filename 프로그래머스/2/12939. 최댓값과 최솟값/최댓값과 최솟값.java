import java.io.*;
import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] str = s.split(" ");
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i=0; i<str.length; i++) {
            arr.add(Integer.parseInt(str[i]));
        }
        
        Collections.sort(arr);
        int min = arr.get(0);
        int max = arr.get(arr.size() - 1);
        
        return min + " " + max;
    }
}
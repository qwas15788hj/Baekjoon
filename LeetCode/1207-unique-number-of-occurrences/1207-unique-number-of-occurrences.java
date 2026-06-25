import java.util.*;
import java.io.*;
class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        int n = arr.length;
        HashMap<Integer, Integer> map1 = new HashMap<>();
        for(int i=0; i<n; i++) {
            map1.put(arr[i], map1.getOrDefault(arr[i], 0) + 1);
        }

        HashMap<Integer, Integer> map2 = new HashMap<>();
        for(Map.Entry<Integer, Integer> entry : map1.entrySet()) {
            if(map2.containsKey(entry.getValue())) {
                return false;
            } else {
                map2.put(entry.getValue(), 1);
            }
        }
        
        return true;
    }
}
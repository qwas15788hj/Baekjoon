import java.util.*;
import java.io.*;
class Solution {
    public boolean closeStrings(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        HashMap<String, Integer> map1 = new HashMap<>();
        HashMap<String, Integer> map2 = new HashMap<>();

        for(int i=0; i<n; i++) {
            String c = word1.charAt(i) + "";
            map1.put(c, map1.getOrDefault(c, 0) + 1);
        }
        for(int i=0; i<m; i++) {
            String c = word2.charAt(i) + "";
            map2.put(c, map2.getOrDefault(c, 0) + 1);
        }

        if(!map1.keySet().equals(map2.keySet())) return false;

        List<Integer> arr1 = new ArrayList<>(map1.values());
        List<Integer> arr2 = new ArrayList<>(map2.values());
        Collections.sort(arr1);
        Collections.sort(arr2);
        if(!arr1.equals(arr2)) return false;

        return true;
    }
}
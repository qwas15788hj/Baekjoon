import java.util.*;
import java.io.*;
class Solution {
    public int minElement(int[] nums) {
        int n = nums.length;
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i=0; i<n; i++) {
            String s = String.valueOf(nums[i]);
            int m = s.length();
            int check = 0;
            for(int j=0; j<m; j++) {
                check += s.charAt(j) - '0';
            }
            arr.add(check);
        }
        
        return Collections.min(arr);
    }
}
import java.util.*;
import java.io.*;
class Solution {
    public void moveZeroes(int[] nums) {
        int idx = 0;
        int n = nums.length;
        int[] arr = new int[n];
        for(int i=0; i<n; i++) {
            if(nums[i] != 0) {
                arr[idx] = nums[i];
                idx += 1;
            }
        }
        for(int i=0; i<n; i++) {
            nums[i] = arr[i];
        }
    }
}
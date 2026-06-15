import java.io.*;
import java.util.*;
class Solution {
    public int pivotIndex(int[] nums) {
        int n = nums.length;
        int left = 0, right = 0;
        for(int i=1; i<n; i++) {
            right += nums[i];
        }

        for(int i=0; i<n; i++) {
            if(left == right) {
                return i;
            }
            if(i == n-1) {
                break;
            }

            left += nums[i];
            right -= nums[i+1];
        }

        return -1;
    }
}
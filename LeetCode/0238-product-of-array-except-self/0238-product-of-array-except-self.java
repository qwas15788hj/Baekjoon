import java.util.*;
import java.io.*;
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int check = 1;
        int zero = 0;
        for(int i=0; i<n; i++) {
            if(nums[i] == 0) {
                zero += 1;
            } else {
                check *= nums[i];
            }
        }

        int[] answer = new int[n];
        for(int i=0; i<n; i++) {
            if(zero >= 2) {
                break;
            } else if(zero == 1) {
                if(nums[i] == 0) {
                    answer[i] = check;
                }
            } else {
                answer[i] = check/nums[i];
            }
        }

        return answer;
    }
}
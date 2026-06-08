import java.io.*;
import java.util.*;
class Solution {
    public int longestOnes(int[] nums, int k) {
        int n = nums.length;
        int left = 0, right = 0;
        int count = 0;
        int answer = 0;

        while(true) {
            if(right == n) {
                break;
            }
            
            if(nums[right] == 0) {
                if(count == k) {
                    while(true) {
                        if(nums[left] == 0) {
                            left += 1;
                            break;
                        }
                        left += 1;
                    }
                } else {
                    count += 1;
                }
            }
            right += 1;
            answer = Math.max(answer, right-left);
        }

        return answer;
    }
}
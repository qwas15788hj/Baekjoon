import java.io.*;
import java.util.*;
class Solution {
    public int longestSubarray(int[] nums) {
        int n = nums.length;
        int left = 0, right = 0;
        int count = 0;
        int answer = 0;

        while(true) {
            if(right == n) {
                break;
            }

            if(nums[right] == 0) {
                if(count == 0) {
                    count += 1;
                } else {
                    while(true) {
                        if(nums[left] == 0) {
                            left += 1;
                            break;
                        }
                        left += 1;
                    }
                }
            }
            right += 1;
            answer = Math.max(answer, right-left-1);
        }

        return answer;
    }
}
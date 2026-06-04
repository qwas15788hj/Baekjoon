import java.io.*;
import java.util.*;
class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int left = 0, right = nums.length-1;
        int answer = 0;
        while(left < right) {
            int sum = nums[left] + nums[right];
            if(sum == k) {
                answer += 1;
                left += 1;
                right -= 1;
            } else if(sum > k) {
                right -= 1;
            } else {
                left += 1;
            }
        }
        return answer;
    }
}
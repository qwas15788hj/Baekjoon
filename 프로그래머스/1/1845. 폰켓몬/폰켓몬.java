import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int n = nums.length;
        Set<Integer> set = new HashSet<Integer>();
        for(int i=0; i<n; i++) {
            set.add(nums[i]);
        }

        return Math.min(set.size(), n/2);
    }
}
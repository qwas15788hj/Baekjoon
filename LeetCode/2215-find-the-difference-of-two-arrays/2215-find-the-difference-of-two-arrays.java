import java.util.*;
import java.io.*;
class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        for(int x : nums1) set1.add(x);
        for(int x : nums2) set2.add(x);

        List<List<Integer>> answer = new ArrayList<>();
        List<Integer> result1 = new ArrayList<>();
        List<Integer> result2 = new ArrayList<>();

        for(int x : set1) {
            if(!set2.contains(x)) result1.add(x);
        }
        for(int x : set2) {
            if(!set1.contains(x)) result2.add(x);
        }

        answer.add(result1);
        answer.add(result2);

        return answer;
    }
}
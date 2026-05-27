import java.util.*;
import java.io.*;
class Solution {
    public String reverseVowels(String s) {
        int n = s.length();
        char[] vowels = {'a','e','i','o','u','A','E','I','O','U'};
        ArrayList<Character> arr = new ArrayList<>();
        ArrayList<Integer> idx = new ArrayList<>();
        for(int i=0; i<n; i++) {
            arr.add(s.charAt(i));
            for(int j=0; j<vowels.length; j++) {
                if(vowels[j] == s.charAt(i)) {
                    idx.add(i);
                }
            }
        }
        
        int size = idx.size();
        for(int i=0; i<size/2; i++) {
            int st = idx.get(i);
            int ed = idx.get(size-1-i);
            arr.set(st, s.charAt(ed));
            arr.set(ed, s.charAt(st));
        }
        
        String answer = "";
        for(int i=0; i<arr.size(); i++) {
            answer += arr.get(i);
        }
        
        return answer;
    }
}
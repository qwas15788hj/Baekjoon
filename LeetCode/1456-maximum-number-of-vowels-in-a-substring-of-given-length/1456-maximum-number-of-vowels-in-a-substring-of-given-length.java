import java.io.*;
import java.util.*;
class Solution {
    public int maxVowels(String s, int k) {
        int n = s.length();
        char[] arr = {'a', 'e', 'i', 'o', 'u'};
        int answer = 0, count = 0;
        for(int i=0; i<k; i++) {
            for(int j=0; j<5; j++) {
                if(s.charAt(i) == arr[j]) {
                    count += 1;
                    answer += 1;
                }   
            }
        }

        for(int i=k; i<n; i++) {
            for(int j=0; j<5; j++) {
                if(s.charAt(i-k) == arr[j]) {
                    count -= 1;
                }
                if(s.charAt(i) == arr[j]) {
                    count += 1;
                }
            }
            answer = Math.max(answer, count);
        }

        return answer;
    }
}
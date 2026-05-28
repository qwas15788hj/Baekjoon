import java.util.*;
import java.io.*;
class Solution {
    public String reverseWords(String s) {
        String[] arr = s.trim().split(" ");
        String answer = "";
        for(int i=arr.length-1; i>-1; i--) {
            if(arr[i].equals("")) continue;
            answer += arr[i] + " ";
        }

        return answer.substring(0, answer.length()-1);
    }
}
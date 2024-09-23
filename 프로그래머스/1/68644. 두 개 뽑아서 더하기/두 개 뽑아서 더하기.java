import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        ArrayList<Integer> arr = new ArrayList<>();
        
        for(int i=0; i<numbers.length; i++) {
            for(int j=i+1; j<numbers.length; j++) {
                int a = numbers[i] + numbers[j];
                if(arr.indexOf(a) < 0) {
                    arr.add(a);
                }
            }
        }
        Collections.sort(arr);
        
        int[] answer = new int[arr.size()];
        for(int i=0; i<arr.size(); i++) {
            answer[i] = arr.get(i);
        }
        
        return answer;
    }
}
import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int scv : scoville) {
            pq.offer(scv);
        }
        
        while(pq.peek() < K) {
            if(pq.size() <= 1) return -1;
            int a = pq.poll();
            int b = pq.poll();
            pq.offer(a + b * 2);
            answer += 1;
        }
        
        return answer;
    }
}
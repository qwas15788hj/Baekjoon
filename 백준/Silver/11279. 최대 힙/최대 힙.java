import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    static Integer n, num;
    static PriorityQueue<Integer> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        for(int i=0; i<n; i++) {
            num = Integer.parseInt(br.readLine());
            if(num == 0) {
                if(pq.size() == 0) {
                    sb.append(0).append("\n");
                } else {
                    sb.append(-pq.poll()).append("\n");
                }
            } else {
                pq.offer(-num);
            }
        }

        System.out.println(sb);
    }

}

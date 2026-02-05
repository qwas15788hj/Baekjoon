import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    static Integer n, x;
    static PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
        if(o1[0] == o2[0]) return o1[1] - o2[1];
        return o1[0] - o2[0];
    });

    public static void main(String[] args) throws IOException {

        n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++) {
            x = Integer.parseInt(br.readLine());
            if(x == 0) {
                if(pq.size() == 0) {
                    sb.append(0).append("\n");
                } else {
                    int[] check = pq.poll();
                    int c1 = check[0];
                    int c2 = check[1];
                    if(c2 == 0) c1 *= -1;
                    sb.append(c1).append("\n");
                }
            } else {
                int num = 1;
                if(x < 0) num = 0;
                pq.offer(new int[] {Math.abs(x), num});
            }
        }

        System.out.println(sb);

    }
}

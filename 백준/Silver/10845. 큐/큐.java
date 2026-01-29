import java.io.*;
import java.util.*;
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    static Integer num;
    static Queue<Integer> queue = new LinkedList<>();
    public static void main(String[] args) throws IOException {

        Integer n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            if(command.equals("push")) {
                num = Integer.parseInt(st.nextToken());
                queue.add(num);
            } else if(command.equals("pop")) {
                if(queue.size() == 0) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(queue.poll()).append("\n");
                }
            } else if(command.equals("size")) {
                sb.append(queue.size()).append("\n");
            } else if(command.equals("empty")) {
                if(queue.size() == 0) {
                    sb.append(1).append("\n");
                } else {
                    sb.append(0).append("\n");
                }
            } else if(command.equals("front")) {
                if(queue.size() == 0) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(queue.peek()).append("\n");
                }
            } else if(command.equals("back")) {
                if(queue.size() == 0) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(num).append("\n");
                }
            }
        }
        System.out.println(sb);
    }
}

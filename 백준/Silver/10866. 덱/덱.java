import java.io.*;
import java.util.*;
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    static Deque<Integer> deque = new ArrayDeque<>();
    public static void main(String[] args) throws IOException {

        Integer n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            if(command.equals("push_front")) {
                deque.addFirst(Integer.parseInt(st.nextToken()));
            } else if(command.equals("push_back")) {
                deque.add(Integer.parseInt(st.nextToken()));
            } else if(command.equals("pop_front")) {
                if(deque.size() == 0) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(deque.poll()).append("\n");;
                }
            } else if(command.equals("pop_back")) {
                if(deque.size() == 0) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(deque.pollLast()).append("\n");;
                }
            } else if(command.equals("size")) {
                sb.append(deque.size()).append("\n");
            } else if(command.equals("empty")) {
                if(deque.size() == 0) {
                    sb.append(1).append("\n");
                } else {
                    sb.append(0).append("\n");
                }
            } else if(command.equals("front")) {
                if(deque.size() == 0) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(deque.peek()).append("\n");;
                }
            } else if(command.equals("back")) {
                if(deque.size() == 0) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(deque.peekLast()).append("\n");;
                }
            }
        }
        System.out.println(sb);
    }
}

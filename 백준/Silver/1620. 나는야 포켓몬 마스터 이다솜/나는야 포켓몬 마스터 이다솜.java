import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    static Integer n, m;
    static HashMap<Integer, String> map1 = new HashMap<>();
    static HashMap<String, Integer> map2 = new HashMap<>();
    static String s;

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        for(int i=0; i<n; i++) {
            s = br.readLine();
            map1.put(i+1, s);
            map2.put(s, i+1);
        }

        for(int i=0; i<m; i++) {
            s = br.readLine();
            if(Character.isDigit(s.charAt(0))) {
                sb.append(map1.get(Integer.parseInt(s))).append("\n");
            } else {
                sb.append(map2.get(s)).append("\n");
            }
        }

        System.out.println(sb);

    }
}

import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    static Integer n, m;
    static int[] arr;
    static boolean[] visited;
    static int[] out;
    static ArrayList<int[]> result = new ArrayList<>();

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n];
        visited = new boolean[n];
        out = new int[m];
        for(int i=0; i<n; i++) {
            arr[i] = i+1;
        }

        permutations(0);
        Collections.sort(result, (o1, o2) -> {
            if(o1[0] == o2[0]) return o1[1] - o2[1];
            return o1[0] - o2[0];
        });

        for(int i=0; i<result.size(); i++) {
            for(int j=0; j<result.get(i).length; j++) {
                sb.append(result.get(i)[j] + " ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    public static void permutations(int cnt) {
        if(cnt == m) {
            result.add(out.clone());
            return;
        }
        for(int i=0; i<n; i++) {
            if(!visited[i]) {
                visited[i] = true;
                out[cnt] = arr[i];
                permutations(cnt+1);
                visited[i] = false;
            }
        }
    }

}

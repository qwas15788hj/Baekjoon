import java.util.*;
import java.io.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws IOException {

        Integer n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for(int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        sb.append(arr[0] + " " + arr[n-1]);
        System.out.println(sb);
    }
}

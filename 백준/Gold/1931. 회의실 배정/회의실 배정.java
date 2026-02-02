import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb = new StringBuffer();
    static Integer n, a, b;
    static int idx;
    static int[][] arr;
    static ArrayList<Integer> room;

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        arr = new int[n][2];
        room = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            arr[i][0] = a;
            arr[i][1] = b;
        }

        Arrays.sort(arr, (o1, o2) -> {
            if(o1[0] == o2[0]) {
                return Integer.compare(o1[1], o2[1]);
            }
            return Integer.compare(o1[0], o2[0]);
        });

        for(int i = 0; i < n; i++) {
            if(room.size() == 0) {
                room.add(arr[i][1]);
                continue;
            }

            idx = room.size()-1;
            if(room.get(idx) > arr[i][1]) {
                room.remove(idx);
                room.add(arr[i][1]);
            } else if(room.get(idx) <= arr[i][0]) {
                room.add(arr[i][1]);
            }
        }

        System.out.println(room.size());
    }
}

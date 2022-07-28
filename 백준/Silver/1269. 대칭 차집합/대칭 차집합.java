import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		StringTokenizer st = new StringTokenizer(str, " ");
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		String x = br.readLine();
		String y = br.readLine();
		
		Set<Integer> a = new HashSet<Integer>();
		Set<Integer> b = new HashSet<Integer>();
		StringTokenizer st1 = new StringTokenizer(x, " ");
		StringTokenizer st2 = new StringTokenizer(y, " ");
		for(int i=0; i<n; i++) {
			a.add(Integer.parseInt(st1.nextToken()));
		}
		for(int i=0; i<m; i++) {
			b.add(Integer.parseInt(st2.nextToken()));
		}
		
		Set<Integer> aSub = new HashSet<Integer>(a);
		Set<Integer> bSub = new HashSet<Integer>(b);
		aSub.removeAll(b);
		bSub.removeAll(a);
		
		System.out.println(aSub.size()+bSub.size());
		
	}

}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		ArrayList<String> arr = new ArrayList<>();
		for(int i=0; i<n; i++) {
			arr.add(br.readLine());
		}
		
		Collections.sort(arr, new Comparator<String>(){
			@Override
			public int compare(String o1, String o2) {
				if(o1.length()==o2.length())
					return o1.compareTo(o2);
				else
					return o1.length()-o2.length();
			}
		});
		for(int i=0; i<arr.size(); i++) {
			if(i!=0) {
				if(arr.get(i).compareTo(arr.get(i-1)) != 0)
					System.out.println(arr.get(i));
			}
			else
				System.out.println(arr.get(i));
		}
		
	}

}

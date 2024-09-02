import java.util.*;

public class Main {

	public static void main(String[] args) {
		
		StringBuilder sb = new StringBuilder();
		
		int[] arr = new int[10001];
		for(int i=1; i<10001; i++) {
			int num = i;
			String s = Integer.toString(i);
			for(int j=0; j<s.length(); j++) {
				num += s.charAt(j) - '0';
			}
			if(num < arr.length) {
				arr[num]++;
			}
		}
		
		for(int i=1; i<arr.length; i++) {
			if(arr[i] == 0) {
				sb.append(i).append('\n');
			}
		}
		
		System.out.println(sb);
	}

}

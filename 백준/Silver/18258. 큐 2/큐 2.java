import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		Queue q = new LinkedList<>();
		int back = 0;
		for(int i=0; i<n; i++) {
			String[] command = br.readLine().split(" ");
			if(command[0].equals("push")) {
				q.offer(Integer.parseInt(command[1]));
				back = Integer.parseInt(command[1]);
			} else if(command[0].equals("pop")) {
				if(q.size()==0) sb.append(-1).append('\n');
				else sb.append(q.poll()).append('\n');
			} else if(command[0].equals("size")) {
				sb.append(q.size()).append('\n');
			} else if(command[0].equals("empty")) {
				if(q.size()==0) sb.append(1).append('\n');
				else sb.append(0).append('\n');
			} else if(command[0].equals("front")) {
				if(q.size()==0) sb.append(-1).append('\n');
				else sb.append(q.peek()).append('\n');
			} else {
				if(q.size()==0) sb.append(-1).append('\n');
				else sb.append(back).append('\n');
			}
 
		}//for
		System.out.println(sb);
		
	}//main
	
}//class
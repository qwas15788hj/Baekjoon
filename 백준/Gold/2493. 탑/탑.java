import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		Stack<int[]> stack = new Stack<>();
		StringBuilder sb = new StringBuilder();
		
		for(int i=1; i<=n; i++) {
			int height = Integer.parseInt(st.nextToken());
			
			while(!stack.empty()) {
				if(stack.peek()[1] > height) { //받을 것이 있다.
					sb.append(stack.peek()[0]+" ");
					break;
				}
				stack.pop(); //못받는 스택은 꺼냄
			}//while(stack_check)
			
			if(stack.empty()) { //스택이 비었으면 받을 것이 없다.
				sb.append("0 ");
			}
			//스택에 추가
			stack.push(new int[] {i, height});
			
		}//for(command)
		System.out.println(sb);
		
	}//main
}//end class
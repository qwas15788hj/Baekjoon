import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

public class Main {
	
	static int n;
	static char[] arr; //식
	static int[] store; //저장
	static Boolean[] select; //뽑았는지
	static int[] num; //연산자 번호
	static boolean flag;
	static ArrayList<Boolean[]> oper = new ArrayList<>(); //연산정보
	static int answer = Integer.MIN_VALUE;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		String str = br.readLine();
		arr = new char[str.length()];
		for(int i=0; i<str.length(); i++) {
			arr[i] = str.charAt(i);
		}
		
		select = new Boolean[n/2];
		num = new int[n/2];
		for(int i=0; i<n/2; i++) {
			num[i] = i;
		}
		
		subset(0);
		
//		for(int i=0; i<oper.size(); i++) {
//			System.out.println(Arrays.toString(oper.get(i)));
//		}
		for(int i=0; i<oper.size(); i++) {
			check(oper.get(i));
		}
		
		System.out.println(answer);

	}//main
	
	private static void subset(int index) {
		if(index==n/2) {
			flag = true;
			for(int i=0; i<n/2-1; i++) {
				if(select[i] && select[i+1]) {
//					System.out.println(Arrays.toString(select));
					flag = false;
					break;
				}
			}//for
			
//			Boolean[] to_oper = new Boolean[n/2];
			if(flag) {
//				System.out.println("맞는것: "+Arrays.toString(select));
				oper.add(Arrays.copyOfRange(select, 0, select.length));
			}
			
			return;
			
		}//if
		
		
		select[index] = true;
		subset(index+1);
		
		select[index] = false;
		subset(index+1);
	}
	
	private static void check(Boolean[] op) {
		Stack<String> st = new Stack<>();
		boolean next = false;
		int spop = 0;
		int sarr = 0;
		for(int i=0; i<arr.length; i++) {
			if(arr[i]=='+' || arr[i]=='-' || arr[i]=='*') { //연산자면
				if(op[i/2]) { //true면
					spop = Integer.parseInt(st.pop());
					sarr = arr[i+1]-'0';
					if(arr[i]=='+') {
						st.push(Integer.toString(spop+sarr));
					}
					else if(arr[i]=='-') {
						st.push(Integer.toString(spop-sarr));
					}
					else if(arr[i]=='*') {
						st.push(Integer.toString(spop*sarr));
					}
					next = true;
				} else { //false면
					st.push(Character.toString(arr[i]));
				}
			} else { //연산자 아니면
				if(!(next)) {
					st.push(Character.toString(arr[i]));
				} else {
					next = false;
				}
			}
//			System.out.println(st);
		}//for
		
		String[] calArr = new String[st.size()];
		for(int i=st.size()-1; i>=0; i--) {
			calArr[i] = st.pop();
		}
		
//		System.out.println(Arrays.toString(calArr));
		int sum = Integer.parseInt(calArr[0]);
		for(int i=1; i<calArr.length; i++) {
			if(calArr[i].equals("+")) sum+=Integer.parseInt(calArr[i+1]);
			else if(calArr[i].equals("-")) sum-=Integer.parseInt(calArr[i+1]);
			else if(calArr[i].equals("*")) sum*=Integer.parseInt(calArr[i+1]);
		}
//		System.out.println(sum);
		answer = Math.max(answer, sum);
	}//op
	

}//class

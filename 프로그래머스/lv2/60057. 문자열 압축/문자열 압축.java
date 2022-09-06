class Solution {
    public int solution(String s) {
		// String s = "xababcdcdababcdcd";
		int answer = s.length();
		
		for(int i=1; i<s.length()/2+1; i++) {
			String pre = s.substring(0, i);
			int count = 0;
			String word = "";
			// System.out.println("12312312"+s.substring(0, i));
			for(int j=0; j<s.length(); j+=i) {
				String now = "";
				if(j+i>s.length()) {
					now = s.substring(j, s.length());
				} else {
					now = s.substring(j, j+i);
				}
				// System.out.println(now);
				if(pre.equals(now)) count += 1;
				else {
					if(count>1) {
						word += Integer.toString(count) + pre;
					}
					else {
						word += pre;
					}
					
					pre = now;
					count = 1;
				}
			
			}
			
			if(count>1) {
				word += Integer.toString(count) + pre;
			} else {
				word += pre;
			}
			
			answer = Math.min(answer, word.length());
			
		}
		
		// System.out.println(answer);
        return answer;
    }
}
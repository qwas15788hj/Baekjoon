import java.util.*;

class Solution {
    public String[] solution(String[] record) {
		ArrayList<String> result = new ArrayList<>();
		HashMap<String, String> user = new HashMap<>();
		
		// String[] record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"};
		StringTokenizer st;
		for(String r: record) {
			st = new StringTokenizer(r);
			String command = st.nextToken();
			String userId = st.nextToken();
			String nickname = "";
			if(!command.equals("Leave")) {
				nickname = st.nextToken();
				user.put(userId, nickname);
			}
			
		}
		
		for(String r: record) {
			st = new StringTokenizer(r);
			String command = st.nextToken();
			String userId = st.nextToken();
			
			switch(command) {
			case "Enter":
				result.add(user.get(userId)+"님이 들어왔습니다.");
				break;
			case "Leave":
				result.add(user.get(userId)+"님이 나갔습니다.");
				break;
			case "Change":
				break;
			}
			
		}
        
		String[] result2 = new String[result.size()];
		for(int i=0; i<result.size(); i++) {
			result2[i] = result.get(i);
		}
        
        return result2;
    }
}
class Solution {
    public int compress(char[] chars) {
        int n = chars.length;
        if(n == 1) {
            return 1;
        }

        char c = chars[0];
        int count = 1;
        ArrayList<String> arr = new ArrayList<>();
        int answer = 0;
        for(int i=1; i<n; i++) {
            if(chars[i] == c) {
                count += 1;
            } else {
                arr.add(c + "");
                if(count != 1) {
                    String s_cnt = Integer.toString(count);
                    for(int j=0; j<s_cnt.length(); j++) {
                        arr.add(s_cnt.charAt(j) + "");
                    }
                }
                c = chars[i];
                count = 1;
            }
        }
        
        arr.add(c + "");
        if(count != 1) {
            String s_cnt = Integer.toString(count);
            for(int j=0; j<s_cnt.length(); j++) {
                arr.add(s_cnt.charAt(j) + "");
            }
        }

        for(int i=0; i<arr.size(); i++) {
            chars[i] = arr.get(i).charAt(0);
        }

        return arr.size();
    }
}
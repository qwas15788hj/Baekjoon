class Solution {
    public String mergeAlternately(String word1, String word2) {
        String answer = "";
        int n = word1.length();
        int m = word2.length();
        int min = Math.min(n, m);

        for(int i=0; i<min; i++) {
            answer += word1.charAt(i);
            answer += word2.charAt(i);
        }
        answer += word1.substring(min, n);
        answer += word2.substring(min, m);

        return answer;
    }
}
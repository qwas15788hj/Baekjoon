class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        low, up = [-1] * 26, [-1] * 26
        for i in range(n):
            num = ord(word[i])
            if 97 <= num <= 122:
                low[num-97] = i
            if 65 <= num <= 90 and up[num-65] == -1:
                up[num-65] = i
        
        answer = 0
        for i in range(26):
            if low[i] != -1 and up[i] != -1 and up[i] > low[i]:
                answer += 1

        return answer
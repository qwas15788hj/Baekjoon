class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        low, up = [False]*26, [False]*26
        for i in range(n):
            num = ord(word[i])
            if 65 <= num <= 90:
                low[num-65] = True
            if 97 <= num <= 122:
                up[num-97] = True
        
        answer = 0
        for i in range(26):
            if low[i] and up[i]:
                answer += 1
    
        return answer
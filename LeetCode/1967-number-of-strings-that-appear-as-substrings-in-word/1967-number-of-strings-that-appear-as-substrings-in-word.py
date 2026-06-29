class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        answer = 0
        for p in patterns:
            if p in word:
                answer += 1
                
        return answer
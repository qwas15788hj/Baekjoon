class Solution:
    def minimumPushes(self, word: str) -> int:
        arr = [0] * 26
        for w in word:
            arr[ord(w)-97] += 1
        arr.sort(reverse=True)
        
        answer = 0
        for i in range(4):
            answer += sum(arr[i*8 : min((i+1)*8, len(arr))]) * (i+1)

        return answer
        
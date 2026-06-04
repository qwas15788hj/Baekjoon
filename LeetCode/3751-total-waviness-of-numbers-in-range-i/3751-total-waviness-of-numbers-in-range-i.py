class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        answer = 0
        for num in range(num1, num2+1):
            s = str(num)
            for i in range(1, len(s)-1):
                if int(s[i]) > int(s[i-1]) and int(s[i]) > int(s[i+1]):
                    answer += 1
                if int(s[i]) < int(s[i-1]) and int(s[i]) < int(s[i+1]):
                    answer += 1

        return answer
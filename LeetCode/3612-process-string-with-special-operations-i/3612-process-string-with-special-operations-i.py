class Solution:
    def processStr(self, s: str) -> str:
        answer = ""
        for i in s:
            if i == "*":
                if len(answer) > 0:
                    answer = answer[:-1]
            elif i == "#":
                if len(answer) > 0:
                    answer += answer
            elif i == "%":
                if len(answer) > 0:
                    answer = answer[::-1]
            else:
                answer += i
                
        return answer
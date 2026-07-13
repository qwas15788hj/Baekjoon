class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        arr = []
        for i in range(2, 10):
            for j in range(9-i+1):
                arr.append(int("".join(num[j:j+i])))
        
        answer = []
        for a in arr:
            if low <= a <= high:
                answer.append(a)

        return answer
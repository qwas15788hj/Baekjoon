class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        num = ""
        for i in range(n):
            num += str(digits[i])
        num = str(int(num) + 1)
        
        arr = []
        for i in range(len(num)):
            arr.append(int(num[i]))
        
        return arr
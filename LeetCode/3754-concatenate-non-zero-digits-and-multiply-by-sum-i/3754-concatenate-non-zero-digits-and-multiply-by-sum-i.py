class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
            
        x = ""
        s = str(n)
        for i in range(len(s)):
            if s[i] != '0':
                x += s[i]
        
        sumx = 0
        for i in range(len(x)):
            sumx += int(x[i])
        
        return int(x) * sumx
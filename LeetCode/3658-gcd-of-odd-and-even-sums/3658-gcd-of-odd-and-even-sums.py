class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        x, y = 0 , 0
        idx = 1
        for _ in range(n):
            x += idx
            idx += 1
            y += idx
            idx += 1
        
        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a
        
        return gcd(x, y)
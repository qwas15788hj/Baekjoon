class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a
        
        mx = 0
        result = []
        for num in nums:
            mx = max(mx, num)
            result.append(gcd(num, mx))
        
        result.sort()
        answer = 0
        for i in range(len(result)//2):
            answer += gcd(result[i], result[-(i+1)])
        
        return answer
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for num in nums:
            arr = []
            for i in range(1, int(num**0.5)+1):
                if num%i == 0:
                    arr.append(i)
                    
            if len(arr) == 2 and arr[-1]**2 != num:
                for a in arr:
                    answer += a
                    answer += num//a
        
        return answer
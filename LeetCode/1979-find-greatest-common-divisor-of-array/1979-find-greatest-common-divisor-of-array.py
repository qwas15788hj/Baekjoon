class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        
        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a
        
        return gcd(nums[0], nums[-1])
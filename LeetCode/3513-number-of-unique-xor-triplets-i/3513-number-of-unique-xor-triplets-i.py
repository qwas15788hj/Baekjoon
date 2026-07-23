class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        
        num = max(nums)
        return 2**len(str(bin(num))[2:])
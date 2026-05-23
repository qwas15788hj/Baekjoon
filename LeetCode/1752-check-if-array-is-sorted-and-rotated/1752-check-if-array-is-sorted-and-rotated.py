from collections import deque

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sorted(nums)
        for _ in range(n):
            if nums == target:
                return True
            nums.append(nums.pop(0))
        
        return False
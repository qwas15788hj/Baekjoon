from collections import deque

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        queue = deque(nums)
        for cnt in range(n+1):
            if queue[0] == target:
                return cnt
            queue.append(queue.popleft())
        
        return -1
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = (nums[-1]-nums[2])
        answer = min(answer, nums[-3]-nums[0])
        answer = min(answer, nums[-2]-nums[1])
        
        return answer
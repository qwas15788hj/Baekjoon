class Solution(object):
    def leftRightDifference(self, nums):
        nums = [0] + nums
        left, right = 0, sum(nums)
        answer = []
        for i in range(1, len(nums)):
            left += nums[i-1]
            right -= nums[i]
            answer.append(abs(left-right))
        
        return answer
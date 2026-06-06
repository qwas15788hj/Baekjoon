class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left, right = [], []
        n = 0
        for num in nums:
            left.append(n)
            n += num
        
        nums = nums[::-1]
        n = 0
        for num in nums:
            right.append(n)
            n += num
        right = right[::-1]
        
        answer = [0] * len(nums)
        for i in range(len(nums)):
            answer[i] = abs(left[i]-right[i])
        
        return answer
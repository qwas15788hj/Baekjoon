class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n, t = len(nums), nums[len(nums)//2]
        answer = 0
        for i in range(n):
            answer += abs(nums[i] - t)

        return answer
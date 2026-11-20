class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 1
        cnt = 1
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                cnt += 1
            else:
                answer = max(answer, cnt)
                cnt = 1
        answer = max(answer, cnt)

        cnt = 1
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                cnt += 1
            else:
                answer = max(answer, cnt)
                cnt = 1
        answer = max(answer, cnt)

        return answer
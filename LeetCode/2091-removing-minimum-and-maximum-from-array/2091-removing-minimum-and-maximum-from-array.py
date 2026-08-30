class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        idx1 = nums.index(max(nums))
        idx2 = nums.index(min(nums))

        if idx1 > idx2:
            idx1, idx2 = idx2, idx1
        
        answer = 1e9
        answer = min(answer, idx2+1)
        answer = min(answer, n-idx1)
        answer = min(answer, (idx1+1)+(n-idx2))

        return answer
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        answer = []
        for i in range(n-1):
            s, e = nums[i], nums[i+1]
            if (e-1) != 1:
                for j in range(s+1, e):
                    answer.append(j)
        
        return answer
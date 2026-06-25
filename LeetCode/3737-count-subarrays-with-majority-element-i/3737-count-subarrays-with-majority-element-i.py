class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        answer = nums.count(target)
        for idx in range(2, len(nums)+1):
            cnt = nums[:idx].count(target)
            if cnt*2 > idx:
                answer += 1
            for i in range(len(nums)-idx):
                if nums[i] == target:
                    cnt -= 1
                if nums[i+idx] == target:
                    cnt += 1
                if cnt*2 > idx:
                    answer += 1
                    
        return answer
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        dic = dict()
        for num in nums:
            dic[num] = 1
        
        answer = 1
        while True:
            num = k*answer
            if num not in dic:
                return num
            answer += 1
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        arr = [0]
        for i in range(len(nums)):
            arr.append(nums[i] + arr[-1])
        
        answer = 1e9
        for i in range(l, r+1):
            for j in range(len(arr)-i):
                num = arr[j+i] - arr[j]
                if num > 0:
                    answer = min(answer, num)

        if answer == 1e9:
            answer = -1

        return answer
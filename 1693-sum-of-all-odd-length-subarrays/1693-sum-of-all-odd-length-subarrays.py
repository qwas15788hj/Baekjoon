from itertools import combinations

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        answer = 0
        arr = [0] + arr
        for i in range(1, len(arr), 2):
            num = sum(arr[:i])
            for j in range(i, len(arr)):
                num += (arr[j] - arr[j-i])
                answer += num
        
        return answer
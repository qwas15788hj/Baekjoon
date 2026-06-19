class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            if num%2 == 0:
                answer.append(-1)
            else:
                s = list(str(bin(num))[2:])
                idx = 0
                for i in range(len(s)-1, -1, -1):
                    if s[i] == '0':
                        idx = i+1
                        break
                s[idx] = '0'
                answer.append(int("".join(s), 2))
    
        return answer
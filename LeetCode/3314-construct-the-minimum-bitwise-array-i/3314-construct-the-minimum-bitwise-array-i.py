class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            b1 = bin(num)
            for x in range(1, num):
                b2 = bin(x|(x+1))
                if b1 == b2:
                    answer.append(x)
                    break
            else:
                answer.append(-1)
        
        return answer
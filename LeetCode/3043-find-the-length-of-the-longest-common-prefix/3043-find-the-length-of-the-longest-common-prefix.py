class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        n, m = len(arr1), len(arr2)
        dic = dict()
        for i in range(n):
            s = str(arr1[i])
            for j in range(len(s)):
                dic[s[:j+1]] = 1
        
        answer = 0
        for i in range(m):
            s = str(arr2[i])
            for j in range(len(s)):
                if s[:j+1] in dic:
                    answer = max(answer, len(s[:j+1]))
                else:
                    break
        
        return answer
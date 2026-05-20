class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        answer = [0] * n
        cnt = 0
        dic1, dic2 = dict(), dict()
        for i in range(n):
            dic1[A[i]] = 1
            dic2[B[i]] = 1
            arr = []
            for k, v in dic1.items():
                if k in dic2:
                    cnt += 1
                    arr.append(k)
            
            for a in arr:
                del dic1[a]

            answer[i] = cnt
    
        return answer
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        arr = [0] + arr
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        
        odd, even, answer = 0, 0, 0
        for i in range(len(arr)):
            num = arr[i]
            # 홀수면, 짝수 개수 answer에 추가
            if num%2 != 0:
                answer += even
                odd += 1
            else:
                answer += odd
                even += 1
            answer %= 1000000007

        return answer%1000000007
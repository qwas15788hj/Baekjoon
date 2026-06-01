class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort(reverse=True)
        answer = 0
        for i in range(n):
            if (i+1)%3 != 0:
                answer += cost[i]
        
        return answer
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # 각각 구매보다 Both구매가 싸거나 같을 경우 -> 먼저 중복인 min을 구매
        if cost1 + cost2 >= costBoth:
            cnt = min(need1, need2)
            result = cnt * costBoth
            # 1이 남았다면
            if need1 > cnt:
                # Both가 싸면 Both가격으로
                if cost1 >= costBoth:
                    result += (need1-cnt) * costBoth
                else:
                    result += (need1-cnt) * cost1

            # 2가 남았다면 동일하게 진행
            if need2 > cnt:
                if cost2 >= costBoth:
                    result += (need2-cnt) * costBoth
                else:
                    result += (need2-cnt) * cost2
            
            return result

        # 각각 구매가 Both구매 보다 쌀 경우 -> 각각 구매
        else:
            return cost1 * need1 + cost2 * need2
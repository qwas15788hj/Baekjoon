class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 1000000007
        n, m = len(s), len(queries)
        val, cnt, num = [0] * n, [0] * n, [0] * n
        if s[0] != '0':
            val[0] = int(s[0])%mod
            cnt[0] = 1
            num[0] = int(s[0])

        for i in range(1, n):
            if s[i] != '0':
                v = (val[i-1]*10+int(s[i])) % mod
                val[i] = v
                cnt[i] = cnt[i-1] + 1
                num[i] = num[i-1] + int(s[i])
            else:
                val[i] = val[i-1]
                cnt[i] = cnt[i-1]
                num[i] = num[i-1]
        
        answer = []
        for s, e in queries:
            if s == 0:
                x = num[e]
                y = val[e]
            else:
                x = num[e] - num[s-1]
                gap = cnt[e] - cnt[s-1]
                y = val[e] - (val[s-1]*pow(10, gap, mod)) % mod

            answer.append((x*y) % mod)

        return answer

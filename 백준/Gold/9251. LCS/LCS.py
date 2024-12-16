# 백준 9251
# 최장 공통 부분수열 (LCS)
import sys
input = sys.stdin.readline
s1 = input().strip()
s2 = input().strip()
d = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])
print(d[-1][-1])
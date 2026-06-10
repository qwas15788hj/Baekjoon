# 합 체크
def check(arr):
    p = len(arr)
    num = sum(arr[0])

    # 가로
    for i in range(p):
        if sum(arr[i]) != num:
            return False

    # 세로
    for i in range(p):
        n = 0
        for j in range(p):
            n += arr[j][i]
        if n != num:
            return False

    # 대각선
    n = 0
    for i in range(p):
        n += arr[i][i]
    if n != num:
        return False

    # 역대각선
    n = 0
    for i in range(p):
        n += arr[i][p-i-1]
    if n != num:
        return False

    return True

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for k in range(min(n, m), 1, -1):
            for i in range(n-k+1):
                for j in range(m-k+1):
                    a = []
                    for x in range(i, i+k):
                        a.append(grid[x][j:j+k])
                    if check(a):
                        return k
        
        return 1
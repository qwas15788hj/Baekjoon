def solution(info, n, m):
    answer = -1
    
    dp = [[1e9] * 121 for _ in range(len(info)+1)]
    dp[0][0] = 0
    for i in range(len(info)):
        a, b = info[i][0], info[i][1]
        for j in range(121):
            if j-a >= 0:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-a])
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + b)
        
    for i in range(121):
        if i < n and dp[-1][i] < m:
            answer = i
            break
    
    return answer
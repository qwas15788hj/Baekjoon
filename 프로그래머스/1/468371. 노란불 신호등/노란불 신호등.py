def solution(signals):
    n = len(signals)
    arr = [] # 각 신호등마다 노란불 -> o / 초록,빨간불 -> x 저장할 배열
    # 절대 만날 수 없는 경우
    for g, y, r in signals:
        if g != r and [r, y, g] in signals:
            return -1
        arr.append('x'*g + 'o'*y + 'x'*r)
    
    time, cycle, yellow = 0, 0, 0 # 현재 시간, 노란불 주기, 노란불 지속시간
    for i in range(n):
        if signals[i][0] + signals[i][2] > cycle:
            time = signals[i][0]
            cycle = signals[i][0] + signals[i][2]
            yellow = signals[i][1]
    
    time -= 1
    while True:
        for _ in range(yellow):
            time += 1
            s = ''
            # 각 신호등마다 현재 시간에 노란색인지 체크
            for i in range(n):
                s += (arr[i][time%len(arr[i])])
            
            if 'x' not in s:
                return time + 1
                
        time += cycle
        
        if time >= 20**5:
            return -1
        
# def solution(signals):
#     n = len(signals)
#     # 절대 만날 수 없는 경우
#     for g, y, r in signals:
#         if g != r and [r, y, g] in signals:
#             return -1
    
#     time = 1
#     arr = [0] * n # 0 -> G / 1 -> Y / 2 -> R
#     count = [1] * n # 각 신호등마다 현재 불빛이 몇 초동안 켜져있었는지
#     while True:
#         time += 1
#         # 각 신호등이 몇 초동안 켜져있었는지
#         for i in range(n):
#             # 현재 켜져있는 빛이 아직 그 시간을 못채웠다면
#             if count[i] != signals[i][arr[i]]:
#                 count[i] += 1
#             # 현재 켜져있는 빛 변경
#             else:
#                 arr[i] = (arr[i] + 1)%3
#                 count[i] = 1
        
#         if arr.count(1) == n:
#             break
        
#         if time > 10**7:
#             return -1
        
#     return time
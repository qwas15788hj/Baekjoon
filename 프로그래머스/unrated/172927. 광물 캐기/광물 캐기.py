def solution(picks, minerals):
    answer = 0
    
    # 곡괭이보다 광물이 많으면 캘수 있는 만큼으로 광물 범위 줄이기
    if len(minerals) > sum(picks) * 5:
        minerals = minerals[:sum(picks) * 5]
        
    # dia, iron, stone 순으로 5개씩 묶기
    arr = [[0, 0, 0] for _ in range(10)]
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            arr[i//5][0] += 1
        elif minerals[i] == "iron":
            arr[i//5][1] += 1
        else:
            arr[i//5][2] += 1
            
    # dia, iron, stone 순으로 많은 것으로 정렬
    arr.sort(key=lambda x:(-x[0], -x[1], -x[2]))
    
    # 현재 캘 차례의 광물을 돌며
    for mineral in arr:
        dia, iron, stone = mineral
        # 현재 사용할 곡괭이 선택
        for i in range(len(picks)):
            # 현재 곡괭이가 0번이며, 0번인 다이아가 1개 이상이면
            if i == 0 and picks[i] > 0:
                answer += dia + iron + stone
                picks[i] -= 1
                break
           # 현재 곡괭이가 1번이며, 1번인 철이 1개 이상이면 
            elif i == 1 and picks[i] > 0:
                answer += dia * 5 + iron + stone
                picks[i] -= 1
                break
            # 현재 곡괭이가 2번이며, 2번인 돌이 1개 이상이면
            elif i == 2 and picks[i] > 0:
                answer += dia * 25 + iron * 5 + stone
                picks[i] -= 1
                break
                
    return answer
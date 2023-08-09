from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    # orders 각 요소를 정렬한 후 다시 입력
    for i in range(len(orders)):
        orders[i] = "".join(sorted(orders[i]))
    
    for c_cnt in course: # 각 코스별 요리 개수 하나씩 탐색
        course_list = [] # 모든 코스 리스트
        for order in orders: # orders 하나씩 탐색
            # 현재 손님이 시킨 요리에서 코스에 필요한 개수만큼 조합하여 저장
            course_list += list(combinations(order, c_cnt))
        # 모두 돌았을 때, 코스 요리가 없으면 패스
        if not course_list:
            pass
        # 코스 요리 있으면
        else:
            # 해당 코스 요리 조합이 몇번 나왔는지
            course_list = list(Counter(course_list).most_common())
            max_count = course_list[0][1] # 가장 많이 주문된 코스 요리의 수
            # 가장 많이 주문된 코스 요리 수가 1이 아니면 진행, 1이면 진행 X
            if max_count != 1:
                for c in course_list: # 코스 요리 조합 돌면서
                    if c[1] == max_count: # 해당 코스 요리 조합이 가장 많이 주문된 요리 수와 같으면
                        answer.append("".join(c[0])) # 해당 코스를 하나의 요리로 이름 붙인 후 저장
    
    # 모든 과정 끝난 후 answer 정렬
    answer.sort()
        
    return answer
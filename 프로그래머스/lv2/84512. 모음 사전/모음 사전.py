from itertools import product

def solution(word):
    answer = 0
    
    alpha = ["A", "E", "I", "O", "U"] # 알파벳 배열
    arr = [] # 사전 배열
    for i in range(6): # 1 ~ 5개의 중복순열 생성
        arr += list(product(alpha, repeat = i))
    
    dic = [""] * len(arr) # 사전 배열의 요소를 붙인 새로운 배열 생성
    for i in range(len(arr)):
        dic[i] = "".join(arr[i]) # 요소의 단어를 붙인 새로운 단어
    
    dic.sort() # 정렬
            
    return dic.index(word)
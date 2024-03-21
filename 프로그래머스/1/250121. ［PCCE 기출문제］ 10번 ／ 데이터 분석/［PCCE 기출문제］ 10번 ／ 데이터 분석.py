def solution(data, ext, val_ext, sort_by):
    check = ["code", "date", "maximum", "remain"]
    answer = []
    
    for i in range(len(data)):
        if data[i][check.index(ext)] < val_ext:
            answer.append(data[i])
    
    answer.sort(key=lambda x:x[check.index(sort_by)])
    
    return answer